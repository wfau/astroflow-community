# OpenAI research assistant

This example provides a lightweight research assistant for AstroFlow notebooks
using an OpenAI model. It is intended for researchers who have access to the
OpenAI API and want conversational help while developing Gaia and distributed
data-analysis workflows.

The assistant adds application-managed memory around the otherwise stateless
API. Questions and answers are written to a local JSONL file, a project summary
can be generated and saved, and relevant earlier exchanges are retrieved for
each new question. This makes the conversation reproducible and allows memory
to persist between notebook sessions, including when using a zero data
retention (ZDR) API configuration.

## Contents

- `Coresearcher-OpenAI.ipynb`: an interactive example.
- `research_assistant.py`: importable memory, retrieval, and assistant classes.

## Requirements

Install the `openai` Python package and make an API key available through the
`OPENAI_API_KEY` environment variable. The helper
`load_openai_api_key_from_shell_file("openai_key.txt")` can load it from a local
shell export file. Do not commit that file or the key.

The retriever uses scikit-learn when it is installed and otherwise falls back
to a standard-library token-overlap search.

From a notebook in this directory:

```python
from research_assistant import ResearchAssistant

assistant = ResearchAssistant(model="gpt-5-nano", memory_dir="memory")
assistant.ask("How should I partition this Gaia query?")
```

## Estimating cost

`ResearchAssistant` keeps cumulative token counts in `input_tokens` and
`output_tokens`. Multiply each count by the model's price per million tokens:

```python
# Replace these with the current per-million-token prices for your model.
input_price = 0.05
output_price = 0.40

estimated_cost_usd = (
    assistant.input_tokens * input_price
    + assistant.output_tokens * output_price
) / 1_000_000

print(f"Estimated cost: ${estimated_cost_usd:.6f}")
```

The example prices are for standard `gpt-5-nano` requests at the time of
writing. Check the [official model page](https://developers.openai.com/api/docs/models/gpt-5-nano)
for current prices. This calculation is an estimate: cached input tokens may
have a lower price, and other service tiers or tools may add different charges.

API calls may incur charges, and prompts, retrieved memories, and summaries are
sent to OpenAI. Check the data-handling terms attached to your API account
before including sensitive or unpublished material. The local `memory/`
directory may also contain research context and should not normally be
committed.
