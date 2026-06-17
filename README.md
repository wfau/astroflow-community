# AstroFlow Community

Welcome to the community examples space for AstroFlow, a distributed science
platform for building, running, and sharing scalable scientific workflows.

This repository is intended to grow through examples, discussion, and pull
requests from researchers, engineers, educators, and anyone experimenting with
distributed approaches to scientific computing. It starts as a small skeleton:
a few themed areas where FAQ-style examples can live, with enough structure to
make contributions easy to find and review.

If you are looking for a place to ask questions, please use the [discussions page](https://github.com/wfau/astroflow-community/discussions).

## What This Repository Is For

Use this repository to share practical answers to common questions, backed by
small notebooks or examples:

- Minimal, runnable examples that show how to use AstroFlow in practice.
- Science workflows that demonstrate real analysis patterns.
- Performance experiments, benchmarks, and scaling notes.
- Examples that combine AstroFlow with large language models or agentic tools.
- Reusable templates, notebooks, scripts, or documentation that help others get
  started.

The GitHub Discussions page is the best place for open-ended questions,
roadmap ideas, design conversations, and requests for examples. Pull requests
are the preferred way to contribute concrete examples that match the style used
in this repository: a clear question in a directory README, linked to a small
notebook or example that answers it.

## Repository Structure

```text
.
├── llm/
│   └── README.md
├── performance/
│   ├── README.md
│   ├── dask/
│   │   ├── code_on_workers.ipynb
│   │   ├── README.md
│   │   └── memory_usage.ipynb
│   └── pyspark/
│       ├── code_on_workers.ipynb
│       └── README.md
├── science/
│   └── README.md
└── README.md
```

### `llm/`

FAQ-style examples that explore how AstroFlow can be used with large language
models, agents, retrieval systems, workflow assistants, or AI-supported
scientific analysis.

### `performance/`

FAQ-style examples focused on scaling behavior, benchmarking, backend
comparisons, cluster execution, throughput, memory use, and practical
performance guidance.

### `performance/dask/`

Dask-specific FAQ examples and notes, including local clusters, distributed
clusters, task graphs, arrays, dataframes, and scheduler behavior.

### `performance/pyspark/`

PySpark-specific FAQ examples and notes, including Spark sessions, dataframe
workloads, cluster configuration, partitioning, and execution tuning.

### `science/`

Domain-oriented FAQ examples. These should show meaningful workflows, datasets,
analysis patterns, or reproducible research tasks that can help other scientists
adapt AstroFlow to their own work.

## Contributing Examples

We are actively soliciting contributions as pull requests -- see, e.g. [PR 1](https://github.com/wfau/astroflow-community/pull/1). A good PR should add
or update a question in the relevant directory README and include a notebook or
small example that answers it.

In detail, the workflow to add a PR is to make a new branch in your local copy of `astroflow-community`,
```
git branch my-new-feature
```
then add your changes and commit
```
git add .
git commit -m 'my new feature does X'
git push
```

You may also contribute via file upload through the GitHub interface.

### Adding to FAQs

For short notebook-based examples, add a row to the local `FAQ` table:

```markdown
| Question | Notebook |
|----------|----------|
| How do I answer this practical question? | `example_notebook.ipynb` |
```

### Adding new directories

A good example should be:

- **Focused:** Demonstrates one clear idea or workflow.
- **Runnable:** Includes setup notes, dependencies, and expected commands.
- **Reproducible:** Uses public data, synthetic data, or clear instructions for
  obtaining inputs.
- **Explained:** Describes what the example shows and why it matters.
- **Respectful of resources:** Notes expected runtime, memory use, and any
  cloud or cluster costs where relevant.

When adding an example, prefer a small subdirectory with its own `README.md`.
That local README should explain the purpose, requirements, how to run it, and
what output to expect.

#### Suggested Example Layout

```text
example-name/
├── README.md
├── requirements.txt        # or environment.yml / pyproject.toml
├── data/                   # optional; prefer small or generated data
├── notebooks/              # optional
├── src/                    # optional
└── outputs/                # optional; keep generated outputs small
```

Large datasets, generated artifacts, credentials, and machine-specific files
should not be committed. Link to external data sources or provide scripts that
create small synthetic fixtures.

## Community Guidelines

Please use the discussion space generously:

- Ask questions when an example is unclear.
- Suggest new example areas.
- Share results from trying an example on different hardware or clusters.
- Propose improvements before opening larger pull requests.

This repository should be useful to people with different levels of experience,
from first-time users to experts comparing distributed execution backends. Clear
explanations, small examples, and honest notes about limitations are all valued.

## Status

This repository is currently a starting point. The directory structure is here
to make the first wave of contributions easier to organize, and the conventions
will evolve as the community adds real examples.
