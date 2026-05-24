# Results Summary

This repository contains the following public experiment bundles.

## Scenario Coverage

- 47 YAML scenario definitions across:
  - `patator`
  - `hydra`
  - `medusa`
  - `patator-network`
  - `patator-versions`

## Processed Dataset Coverage

- 9 processed ConCap SSH parquet datasets in `artifacts/data/concap-clean/`
- 4 processed realism parquet datasets in `artifacts/data/realistic-clean/`

## Evaluation Coverage

- 6 curated notebooks:
  - 2 baseline notebooks
  - 2 generalisation notebooks
  - 2 defense notebooks
- 6 exported result trees:
  - `cicids2017-latest/baseline`
  - `cicids2017-latest/generalisation`
  - `cicids2017-latest/defense`
  - `csecicids2018-latest/baseline`
  - `csecicids2018-latest/generalisation`
  - `csecicids2018-latest/defense`
- 78 per-model result CSV files, plus confusion matrices and serialized result
  artifacts

## Representative Public Entry Points

- `artifacts/scenarios/patator/patator_ssh_cic_T10_P.yaml`
- `artifacts/data/concap-clean/patator-ssh-cic.parquet`
- `artifacts/data/realistic-clean/concap-patator-cic.parquet`
- `artifacts/ml-evaluation/results/cicids2017-latest/baseline/random_forest_results.csv`
- `artifacts/ml-evaluation/results/cicids2017-latest/defense/support_vector_machine_results.csv`

## Scope Note

The public branch is designed to expose the curated HsP artifact set in a
compact form. It does not redistribute the third-party benchmark base datasets
or the raw packet captures from the real-world runs.
