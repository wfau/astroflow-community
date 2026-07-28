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

| Backend | Question | Notebook |
|---------|----------|----------|
| Dask | What is available on the Dask server I connected to? | [dask/lay_of_the_land.ipynb](dask/lay_of_the_land.ipynb) |
| Dask | How do I get custom code onto Dask workers? | [dask/code_on_workers.ipynb](dask/code_on_workers.ipynb) |
| Dask | How can I measure memory use and choose a partition size? | [dask/memory_usage.ipynb](dask/memory_usage.ipynb) |
| Dask | How do I rasterize 2D point data with Dask partitions? | [dask/rasterizer.ipynb](dask/rasterizer.ipynb) |
| PySpark | What is available on the Spark server I connected to? | [pyspark/lay_of_the_land.ipynb](pyspark/lay_of_the_land.ipynb) |
| PySpark | How do I deploy code and packages to Spark executors? | [pyspark/code_on_workers.ipynb](pyspark/code_on_workers.ipynb) |
| PySpark | How do I rasterize 2D point data with a PySpark UDF? | [pyspark/rasterizer.ipynb](pyspark/rasterizer.ipynb) |

## How should I choose between PySpark and Dask?

Neither backend is universally faster or simpler. Start with the shape of the
workload, the APIs already used by the project, and the cluster your team can
operate reliably.

| Consideration | Prefer Dask when... | Prefer PySpark when... |
|---------------|---------------------|------------------------|
| Workload | The analysis mixes arrays, pandas-like tables, arbitrary Python functions, delayed tasks, or futures. | The work is primarily structured-data filtering, joins, aggregations, window operations, or SQL. |
| Existing code | The code already uses NumPy, pandas, or Python functions that partition naturally. | The code already uses Spark DataFrames, Spark SQL, Hive-style tables, or JVM data systems. |
| Execution model | You need direct control over Python task graphs, partition-level functions, or interactive futures. | You want Spark SQL to optimize a declarative DataFrame or SQL query plan. |
| Data shape | The workload includes multidimensional arrays or custom scientific data structures. | The data is mostly tabular and has a stable schema. |
| Operations | The team is comfortable tuning Dask chunks, partitions, worker memory, and task-graph size. | The organization already operates Spark and has established monitoring, catalog, and deployment practices. |
| Portability | Staying close to local NumPy/pandas code is important. | Sharing the same execution engine across Python, SQL, Scala, Java, or R is important. |

Dask exposes array, dataframe, delayed, and futures interfaces, with work
represented as Python task graphs; see the
[Dask API overview](https://docs.dask.org/en/stable/api.html) and
[scheduler documentation](https://docs.dask.org/en/stable/scheduling.html).
Spark SQL uses the structure of DataFrame and SQL operations to optimize their
execution and supports common structured-data sources; see the
[Spark SQL and DataFrames guide](https://spark.apache.org/docs/latest/sql-programming-guide)
and [data-source documentation](https://spark.apache.org/docs/latest/sql-data-sources.html).

### A practical default

- Choose **Dask** for Python-native scientific workflows, especially when the
  same analysis combines arrays, dataframes, and custom task-level logic.
- Choose **PySpark** for large, schema-driven table pipelines dominated by SQL,
  joins, aggregations, and integration with an existing Spark platform.
- If both descriptions fit, implement one representative stage in each backend
  and measure end-to-end runtime, peak worker memory, shuffle volume, task or
  stage count, startup overhead, and operational complexity on the intended
  cluster. Avoid deciding from a small local microbenchmark alone.

The paired `lay_of_the_land`, `code_on_workers`, and `rasterizer` notebooks in
this repository are useful starting points because they expose equivalent
deployment concerns in both backends. The Dask memory notebook adds a concrete
workflow for measuring memory and translating that measurement into partition
sizing.
