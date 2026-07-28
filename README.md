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

## Getting a Copy on a Server

From a shell on the server where you want to run the examples, clone the
repository and move into it:

```bash
git clone https://github.com/wfau/astroflow-community.git
cd astroflow-community
```

If your server is already set up with GitHub SSH keys, the SSH form works too:

```bash
git clone git@github.com:wfau/astroflow-community.git
cd astroflow-community
```

If you plan to contribute examples, first
[fork the repository](https://github.com/wfau/astroflow-community/fork), then
clone your fork by replacing `YOUR-USERNAME` below:

```bash
git clone git@github.com:YOUR-USERNAME/astroflow-community.git
cd astroflow-community
```

## Contributing Examples

We actively welcome contributions as pull requests; see, for example,
[PR 1](https://github.com/wfau/astroflow-community/pull/1). A good pull request
should add or update a question in the relevant directory README and include a
notebook or small example that answers it.

Create and switch to a feature branch in your local clone:

```bash
git switch -c my-new-feature
```

Add and commit your changes, then push the branch to your fork:

```bash
git add .
git commit -m "Add an example of X"
git push -u origin my-new-feature
```

Finally, visit your fork on GitHub and select **Compare & pull request** to open
a pull request against `wfau/astroflow-community`.

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

## Community Guidelines

Please use the discussion space generously:

- Ask questions when an example is unclear.
- Suggest new example areas.
- Share results from trying an example on different hardware or clusters.
- Propose improvements before opening larger pull requests.

This repository should be useful to people with different levels of experience,
from first-time users to experts comparing distributed execution backends. Clear
explanations, small examples, and honest notes about limitations are all valued.


## Full Repository Structure

```text
.
├── llm/
│   ├── README.md
│   └── openai/
│       └── research_assistant.py
├── performance/
│   ├── README.md
│   ├── dask/
│   │   ├── README.md
│   │   ├── code_on_workers.ipynb
│   │   ├── lay_of_the_land.ipynb
│   │   ├── memory_usage.ipynb
│   │   └── rasterizer.ipynb
│   └── pyspark/
│       ├── README.md
│       ├── code_on_workers.ipynb
│       ├── lay_of_the_land.ipynb
│       └── rasterizer.ipynb
├── science/
│   ├── README.md
│   ├── add_Rybizki_dataset.ipynb
│   └── counting_gaia_quantities.ipynb
└── README.md
```
