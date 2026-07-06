# Dask Performance FAQ and Examples

This directory is for AstroFlow examples that use Dask as the distributed
execution backend.

Good examples for this area include:

- Local cluster setup and scheduler configuration.
- Scaling from a laptop to a distributed cluster.
- Array, dataframe, or delayed-task workloads.
- Task graph inspection and optimization.
- Memory behavior, spilling, chunk sizing, and partitioning experiments.

Each example should include a short explanation of the Dask setup, the command
used to run it, and the expected resource profile. Where possible, provide a
small local mode so contributors can try the example without access to a larger
cluster.

Use `lay_of_the_land.ipynb` as a first check when connecting to a Dask server:
it surveys the scheduler connection, worker filesystems, writable paths, and
whether worker-local files are visible across the cluster.

If an example requires a specific deployment environment, document it clearly in
the example README.

## FAQ

| Question | Notebook |
|----------|----------|
| How do I do a quick look at memory usage for optimising? | [memory_usage.ipynb](memory_usage.ipynb) |
| What is available on the Dask server I connected to? | [lay_of_the_land.ipynb](lay_of_the_land.ipynb) |
| How do I get custom code onto the workers? | [code_on_workers.ipynb](code_on_workers.ipynb) |
| How do I rasterize 2D point data with Dask partitions? | [rasterizer.ipynb](rasterizer.ipynb) |
