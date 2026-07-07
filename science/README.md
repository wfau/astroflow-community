# Science FAQ and Examples

This directory is for domain-oriented scientific examples that show AstroFlow
being used for real analysis patterns.

Examples here should focus on the scientific workflow first: the question being
asked, the data being used, the processing steps, and the result. The goal is to
help other scientists recognize patterns they can adapt to their own work.

Good examples for this area include:

- Reproducible analysis pipelines.
- Synthetic or public-data demonstrations.
- Domain-specific preprocessing or feature extraction.
- Parameter sweeps, simulations, or ensemble analysis.
- Workflow patterns that move from local exploration to distributed execution.

Each example should include a local `README.md` that explains the scientific
context, dependencies, data access, how to run the workflow, and what outputs to
expect.

Prefer public datasets, small fixtures, or scripts that generate synthetic data.
If a workflow uses restricted data, provide a public or synthetic substitute so
the example remains useful to the community.

The current examples include a notebook for adding the Rybizki Gaia fidelity
catalog and cross-matching it to a filtered Gaia DR3 RVS sample. It shows the
data download, Dask-based table construction, Gaia source filtering, and a
simple percentile check for the `fidelity_v2 = 0.5` threshold.

## FAQ

| Question | Notebook |
|----------|----------|
| How do I add the Rybizki fidelity dataset and cross-match it to Gaia RVS? | [add_Rybizki_dataset.ipynb](add_Rybizki_dataset.ipynb) |
