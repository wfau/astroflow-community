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

The current examples include notebooks for working with Gaia-scale data:
adding the Rybizki Gaia fidelity catalog, comparing Gaia inverse-parallax
distances with Bailer-Jones photogeometric distances, and counting Gaia
quantities with Spark SQL. Together they show distributed table construction,
catalog cross-matching, Gaia source filtering, parallax zero-point correction,
binned summaries, and checks of thresholds or selection functions.

## FAQ

| Question | Notebook |
|----------|----------|
| How do I add the Rybizki fidelity dataset and cross-match it to Gaia RVS? | [add_Rybizki_dataset.ipynb](add_Rybizki_dataset.ipynb) |
| How do Gaia inverse-parallax distances compare with Bailer-Jones photogeometric distances? | [compare_parallax_BailerJones.ipynb](compare_parallax_BailerJones.ipynb) |
| How do I count Gaia source quantities by magnitude with Spark SQL? | [counting_gaia_quantities.ipynb](counting_gaia_quantities.ipynb) |

## Comparing parallaxes with Bailer-Jones distances

[`compare_parallax_BailerJones.ipynb`](compare_parallax_BailerJones.ipynb)
cross-matches Gaia DR3 sources with radial velocities against the Bailer-Jones
et al. (2021) Gaia EDR3 geometric and photogeometric distance catalog. It then
compares the catalog's median photogeometric distances with distances obtained
by inverting both the published and zero-point-corrected Gaia parallaxes.

### Data and runtime requirements

- `DASK_DATA_PATH_GAIA_DR3_SSD` must contain `GDR3_GAIA_SOURCE`.
- `DASK_DATA_PATH_GAIA_EDR3_SSD` must contain `GEDR3DIST`.
- `DASK_SCHEDULER_ADDRESS` may specify the distributed scheduler; otherwise the
  notebook uses the AstroFlow scheduler address.
- The workflow uses Dask DataFrame, pandas, NumPy, Matplotlib,
  `gaiadr3-zeropoint`, and the local `easy2dhist.py` helper.
- The client and workers should use compatible package versions. The captured
  run reports NumPy and `toolz` version mismatches, so check the Dask version
  table before interpreting failures or numerical differences.

The notebook retains only Gaia sources with a reported radial velocity and
distance-catalog rows with a finite `r_med_photogeo`. It also limits the Gaia
columns before joining to reduce repeated I/O. The partition-wise join assumes
that both parquet datasets have matching `source_id` partition boundaries; use
a standard Dask merge if that condition is not guaranteed.

### Processing and outputs

The Gaia DR3 parallax zero point is evaluated from G magnitude, astrometric
colour, ecliptic latitude, and astrometric solution type. Because the correction
and Gaia parallaxes are both in milliarcseconds, the corrected value is
`parallax - zeropoint`. Inputs outside the package's calibrated ranges are
clipped and produce warnings, so those rows require extra care.

The captured run produced 33,581,727 matched rows in
`data/rvs_joined_bailerjones.parquet`. Its density plots compare:

- corrected and uncorrected inverse-parallax distances with the Bailer-Jones
  median photogeometric distance;
- fractional distance residuals over 0--10 kpc; and
- the parallax residual relative to the reported Gaia parallax uncertainty.

Gaia parallaxes are in milliarcseconds, so `1 / parallax` is in kiloparsecs.
This inversion is a diagnostic rather than a recommended estimator for
non-positive or low-signal-to-noise parallaxes.

### Notebook findings

The captured analysis finds substantial disagreement mainly below about
0.2 mas (beyond roughly 5 kpc). Selecting sources with `ruwe > 1.4` does not
reveal a comparable systematic bias; the discrepancies are instead associated
with low-parallax-significance sources. The notebook therefore treats a
parallax-significance cut of 5 as a conservative threshold for using inverted
parallaxes in this sample. These are exploratory results from the saved run,
not a general validation of inverse-parallax distances.
