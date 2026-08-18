# Ollama research assistant

This example provides the same lightweight research-assistant workflow as the
OpenAI example, but runs models through Ollama. It is intended for researchers
who prefer a locally hosted model, want to work without an OpenAI API key, or
need more control over where prompts and conversational memory are processed.

The assistant stores questions and answers in a local JSONL file, maintains a
project summary, retrieves relevant earlier exchanges, and includes recent
conversation turns in each request. The module is self-contained, so it can be
imported directly from this directory without installing AstroFlow as a Python
package.

## Contents

- `Coresearcher-Ollama.ipynb`: an interactive example.
- `research_assistant.py`: importable memory, retrieval, and assistant classes.

## Requirements

Install and run Ollama, install its Python client, and download a model that is
available to the Ollama server. The assistant defaults to `llama3.2`, but any
compatible installed model can be selected.

The retriever uses scikit-learn when it is installed and otherwise falls back
to a standard-library token-overlap search.

From a notebook in this directory:

```python
from research_assistant import ResearchAssistant

assistant = ResearchAssistant(model="llama3.2", memory_dir="memory")
assistant.ask("How should I partition this Gaia query?")
```

With a local Ollama server, prompts do not need to be sent to a hosted model
provider. This depends on how Ollama is configured: a remote server changes the
privacy boundary. Model output also depends on the selected model and local
hardware. The `memory/` directory may contain research context and should not
normally be committed.
