# Reproducibility Guide

This repository is structured as a curated public artifact bundle.

Its primary purpose is to make the HsP scenarios, processed datasets, and
exported evaluation outputs easy to inspect without requiring access to the
full internal research workspace.

## What You Can Audit Directly

- Scenario definitions under `artifacts/scenarios/`
- Processed parquet datasets under `artifacts/data/`
- Exported per-model result CSV files under `artifacts/ml-evaluation/results/`
- Notebook structure and stored workflow logic under
  `artifacts/ml-evaluation/notebooks/`

For many readers, the exported CSV files are the best starting point because
they expose model-level outputs directly without requiring notebook execution.

## What You Need To Re-Execute Notebooks

The notebooks in `artifacts/ml-evaluation/notebooks/` are included as curated
companion artifacts. Re-executing them requires separately obtaining the
underlying benchmark datasets from their original sources.

This public repository does not redistribute those third-party benchmark base
datasets.

## Real-World Comparison Material

The public release keeps the cleaned real-world comparison datasets:

- `artifacts/data/realistic-clean/bare-patator-cic.parquet`
- `artifacts/data/realistic-clean/concap-patator-cic.parquet`

Raw packet captures and unsanitized flow exports are intentionally omitted from
this branch to avoid publishing private network and operator details.

## Lightweight Integrity Check

Run the release-integrity check from the repository root:

```bash
python3 scripts/check_artifacts.py
```

The script verifies the expected public artifact counts and fails if raw packet
capture files are present.
