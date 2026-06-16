"""Importable research assistant utilities extracted from ResearchAssistant.ipynb."""

from __future__ import annotations

from collections import Counter, deque
import json
import os
from pathlib import Path
import re
import subprocess
import time
from typing import Any


class MemoryStore:
    """Simple JSONL-backed memory store for question/answer pairs."""

    def __init__(self, directory: str | Path = "memory") -> None:
        self.directory = Path(directory)
        self.directory.mkdir(exist_ok=True)

        self.qa_file = self.directory / "qa_log.jsonl"
        self.summary_file = self.directory / "summary.txt"

        if not self.summary_file.exists():
            self.summary_file.write_text("", encoding="utf-8")

    def add_qa(
        self,
        question: str,
        answer: str,
        *,
        metadata: dict[str, Any] | None = None,
        timestamp: float | None = None,
    ) -> dict[str, Any]:
        record: dict[str, Any] = {
            "timestamp": time.time() if timestamp is None else timestamp,
            "question": question,
            "answer": answer,
        }

        if metadata:
            record["metadata"] = metadata

        with self.qa_file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

        return record

    def load_all(self) -> list[dict[str, Any]]:
        if not self.qa_file.exists():
            return []

        records = []
        with self.qa_file.open(encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Invalid JSON in {self.qa_file} on line {line_number}"
                    ) from exc

        return records

    def get_summary(self) -> str:
        return self.summary_file.read_text(encoding="utf-8")

    def set_summary(self, summary: str) -> None:
        self.summary_file.write_text(summary, encoding="utf-8")


class Retriever:
    """Retrieve relevant stored QA pairs with TF-IDF, falling back to stdlib search."""

    def __init__(self, memory_store: MemoryStore) -> None:
        self.memory_store = memory_store

    def retrieve(self, query: str, k: int = 3) -> list[dict[str, Any]]:
        records = self.memory_store.load_all()

        if not records:
            return []

        corpus = [
            f"{record.get('question', '')}\n{record.get('answer', '')}"
            for record in records
        ]

        try:
            return self._retrieve_with_sklearn(query, records, corpus, k)
        except ImportError:
            return self._retrieve_with_token_overlap(query, records, corpus, k)

    @staticmethod
    def _retrieve_with_sklearn(
        query: str,
        records: list[dict[str, Any]],
        corpus: list[str],
        k: int,
    ) -> list[dict[str, Any]]:
        import numpy as np
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        vectorizer = TfidfVectorizer()
        matrix = vectorizer.fit_transform(corpus)
        query_vector = vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, matrix)[0]
        indexes = np.argsort(similarities)[::-1][:k]

        return [records[index] for index in indexes]

    @staticmethod
    def _retrieve_with_token_overlap(
        query: str,
        records: list[dict[str, Any]],
        corpus: list[str],
        k: int,
    ) -> list[dict[str, Any]]:
        query_counts = Counter(_tokens(query))

        def score(text: str) -> int:
            text_counts = Counter(_tokens(text))
            return sum(
                min(count, text_counts[token])
                for token, count in query_counts.items()
            )

        ranked = sorted(
            enumerate(corpus),
            key=lambda item: (score(item[1]), -item[0]),
            reverse=True,
        )

        return [records[index] for index, _ in ranked[:k]]


def build_messages(
    system_prompt: str,
    summary: str,
    retrieved: list[dict[str, Any]],
    recent: list[dict[str, str]],
    question: str,
) -> list[dict[str, str]]:
    """Build the message list sent to the OpenAI API."""

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        }
    ]

    if summary.strip():
        messages.append(
            {
                "role": "system",
                "content": f"Current project summary:\n\n{summary}",
            }
        )

    if retrieved:
        memory_text = []

        for i, item in enumerate(retrieved, start=1):
            memory_text.append(
                f"""
Memory {i}

User:
{item['question']}

Assistant:
{item['answer']}
"""
            )

        messages.append(
            {
                "role": "system",
                "content": (
                    "Potentially relevant previous discussions:\n\n"
                    + "\n".join(memory_text)
                ),
            }
        )

    messages.extend(recent)
    messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    return messages


def load_openai_api_key_from_shell_file(
    path: str | Path = "openai_key.txt",
    *,
    env_var: str = "OPENAI_API_KEY",
) -> str:
    """Load OPENAI_API_KEY from a shell-style export file into this Python process."""

    key_file = Path(path)
    if not key_file.exists():
        raise FileNotFoundError(f"Could not find {key_file}")

    result = subprocess.run(
        [
            "sh",
            "-c",
            '. "$1" && eval "printf %s \\"\\$$2\\""',
            "load_openai_api_key_from_shell_file",
            str(key_file),
            env_var,
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    api_key = result.stdout.strip()
    if not api_key:
        raise ValueError(f"{env_var} was not set by {key_file}")

    os.environ[env_var] = api_key
    return api_key


class ResearchAssistant:
    """Research assistant with persistent memory and lightweight retrieval."""

    def __init__(
        self,
        model: str = "gpt-5-nano",
        memory_dir: str | Path = "memory",
        *,
        client: Any | None = None,
        system_prompt: str | None = None,
        recent_limit: int = 10,
    ) -> None:
        if client is None:
            from openai import OpenAI

            client = OpenAI()

        self.client = client
        self.model = model
        self.memory = MemoryStore(memory_dir)
        self.retriever = Retriever(self.memory)
        self.recent: deque[dict[str, str]] = deque(maxlen=recent_limit)
        self.system_prompt = system_prompt or DEFAULT_SYSTEM_PROMPT

    def ask(
        self,
        question: str,
        *,
        print_answer: bool = True,
        remember: bool = True,
    ) -> str:
        summary = self.memory.get_summary()
        retrieved = self.retriever.retrieve(question, k=3)

        messages = build_messages(
            self.system_prompt,
            summary,
            retrieved,
            list(self.recent),
            question,
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )

        answer = response.choices[0].message.content

        self.recent.append({"role": "user", "content": question})
        self.recent.append({"role": "assistant", "content": answer})

        if remember:
            self.memory.add_qa(question, answer)

        if print_answer:
            print(answer)

        return answer

    def update_summary(self, n_recent: int = 50) -> str:
        """Create a compact project summary from recent Q&A pairs."""

        records = self.memory.load_all()

        if not records:
            return ""

        records = records[-n_recent:]

        transcript = "\n".join(
            f"""
User:
{record['question']}

Assistant:
{record['answer']}
"""
            for record in records
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Summarise the following conversation into a concise "
                        "project overview. Include key assumptions, tools used, "
                        "and important technical details."
                    ),
                },
                {
                    "role": "user",
                    "content": transcript,
                },
            ],
        )

        summary = response.choices[0].message.content
        self.memory.set_summary(summary)

        return summary


DEFAULT_SYSTEM_PROMPT = """
You are assisting an astrophysicist.

Assume familiarity with:

- Python
- NumPy
- Dask
- pandas
- galactic dynamics
- simulations

Prefer concise, runnable solutions.
""".strip()


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9_]+", text.lower())
