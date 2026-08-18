# LLM FAQ and examples

This directory contains examples that connect AstroFlow with large language
models, retrieval systems, and AI-supported scientific workflows. Because
AstroFlow is commonly used in JupyterHub notebooks on remote systems, the
examples include the extra memory and provider integration needed to make an
assistant useful across notebook sessions.

The current research-assistant examples share the same workflow:

- Persistent question-and-answer history stored as JSONL.
- A saved project summary that can be refreshed by the model.
- Retrieval of relevant earlier discussions for each question.
- A bounded recent-conversation window.
- A system prompt tailored to astrophysics, Gaia DR3, and distributed Python
  tools.

## Available backends

| Backend | Best suited to | Requirements | Example |
| --- | --- | --- | --- |
| [OpenAI](openai/README.md) | Hosted models and institutional or personal OpenAI API access | OpenAI Python client and `OPENAI_API_KEY` | [`Coresearcher-OpenAI.ipynb`](openai/Coresearcher-OpenAI.ipynb) |
| [Ollama](ollama/README.md) | Locally hosted models and greater control over data processing | Ollama server, Python client, and a downloaded model | [`Coresearcher-Ollama.ipynb`](ollama/Coresearcher-Ollama.ipynb) |

Both implementations expose a similar `ResearchAssistant` API, so notebooks
can switch providers with minimal changes. Their modules are self-contained and
can be imported directly from their respective directories without installing
this repository as a Python package.

## Choosing a backend

Use OpenAI when access to a hosted model and its capabilities is more important
than local execution. API usage may incur costs, and conversation context sent
with a request is processed by the provider according to the terms of the API
account.

Use Ollama when you want to run an available model on infrastructure you
control. This avoids requiring an OpenAI API key, although performance and
quality depend on the selected model and hardware. Privacy also depends on
whether the configured Ollama server is genuinely local or remote.

## Data and reproducibility

The assistants send retrieved history and the current project summary to the
selected model on every question. Treat generated answers as suggestions:
review code and scientific claims before using them in an analysis.

Do not commit API keys, private prompts, generated memory directories, or
sensitive data. Record the provider, model name, model version where available,
and important prompts when reproducibility matters.
