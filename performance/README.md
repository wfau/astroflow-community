# Performance FAQ and Examples

This directory is for examples that explore how AstroFlow behaves under
different execution engines, workloads, data sizes, and cluster configurations.

Use this area for:

- Benchmarks and scaling studies.
- Backend comparisons.
- Scheduler, partitioning, and task-graph experiments.
- Memory, throughput, and runtime investigations.
- Practical tuning notes for local, cloud, or HPC environments.

Performance examples should be careful about reproducibility. Include the
hardware or cluster shape, software versions, dataset size, command used, and
the metric being measured. If results are machine-dependent, say so directly.

Backend-specific examples should usually go in one of the subdirectories:

- `dask/` for Dask-based examples.
- `pyspark/` for PySpark-based examples.

General performance guidance, cross-backend comparisons, and shared fixtures can
live directly under `performance/`.

## FAQ

| Question | Notebook |
|----------|----------|
| How should I choose between pyspark and dask? | |

