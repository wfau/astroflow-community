# PySpark Performance FAQ and Examples

This directory is for AstroFlow examples that use PySpark or Apache Spark as
the distributed execution backend.

Good examples for this area include:

- Creating and configuring Spark sessions.
- Dataframe workloads and partitioning strategies.
- Local, standalone, YARN, Kubernetes, or cloud Spark execution.
- Shuffle-heavy workloads and tuning experiments.
- Comparing Spark behavior with other AstroFlow execution backends.

Each example should document the Spark version, execution mode, configuration,
input data size, and the command used to run the workload. If the example
expects a cluster, include a small local version or explain why local execution
is not representative.

Do not commit cluster credentials, private configuration, or large generated
outputs.

## FAQ

| Question | Notebook |
|----------|----------|
| How do I deploy code and packages to PySpark executors? | [code_on_workers.ipynb](code_on_workers.ipynb) |
