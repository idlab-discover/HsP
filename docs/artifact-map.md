# Artifact Map

This note maps the main public artifact families in this repository to the HsP
questions they support.

It is intentionally narrower than the full internal research workspace. The aim
is to help readers locate the relevant scenarios, processed datasets, notebooks,
and exported outputs that accompany the paper.

## 1. Core SSH HsP Setup

These files capture the main `patator` SSH host-space perturbation families used
throughout the paper.

- Scenario definitions:
  - `artifacts/scenarios/patator/`
- Processed datasets:
  - `artifacts/data/concap-clean/patator-ssh-cic.parquet`
  - `artifacts/data/concap-clean/patator-ssh-cic-cns22.parquet`
  - `artifacts/data/concap-clean/patator-ssh-cic-nodelay.parquet`
  - `artifacts/data/concap-clean/patator-ssh-cic-nodelay-cns22.parquet`
  - `artifacts/data/concap-clean/patator-ssh-giovanni.parquet`

## 2. Additional SSH HsP Families

These files illustrate that HsP effects are not tied to one exact tool or one
exact command string.

- Alternative SSH tool scenarios:
  - `artifacts/scenarios/hydra/`
  - `artifacts/scenarios/medusa/`
- Processed datasets:
  - `artifacts/data/concap-clean/hydra-ssh-cic.parquet`
  - `artifacts/data/concap-clean/medusa-ssh-cic.parquet`

## 3. Network and Environment Variations

These files cover perturbations induced by network conditions or by execution
environment changes.

- Scenario definitions:
  - `artifacts/scenarios/patator-network/`
  - `artifacts/scenarios/patator-versions/`
- Processed datasets:
  - `artifacts/data/concap-clean/patator-network-ssh-cic.parquet`
  - `artifacts/data/concap-clean/patator-versions-ssh-cic.parquet`

## 4. Benchmark-Side Evaluation Bundles

These directories contain the curated notebooks and exported results for the
public benchmark-side evaluation bundle.

### Notebooks

- Baseline:
  - `artifacts/ml-evaluation/notebooks/baseline/cicids2017-latest.ipynb`
  - `artifacts/ml-evaluation/notebooks/baseline/csecicids2018-latest.ipynb`
- Generalisation:
  - `artifacts/ml-evaluation/notebooks/generalisation/cicids2017-latest.ipynb`
  - `artifacts/ml-evaluation/notebooks/generalisation/csecicids2018-latest.ipynb`
- Defense:
  - `artifacts/ml-evaluation/notebooks/defense/cicids2017-latest.ipynb`
  - `artifacts/ml-evaluation/notebooks/defense/csecicids2018-latest.ipynb`

### Exported Result Trees

- `artifacts/ml-evaluation/results/cicids2017-latest/baseline/`
- `artifacts/ml-evaluation/results/cicids2017-latest/generalisation/`
- `artifacts/ml-evaluation/results/cicids2017-latest/defense/`
- `artifacts/ml-evaluation/results/csecicids2018-latest/baseline/`
- `artifacts/ml-evaluation/results/csecicids2018-latest/generalisation/`
- `artifacts/ml-evaluation/results/csecicids2018-latest/defense/`

The CSV files in these directories expose per-model outputs directly and are the
most convenient public entry point for result inspection.

## 5. Real-World SSH Comparison

These files support the bare-metal versus ConCap comparison used to study
whether the SSH HsP behavior persists outside the benchmark-side datasets.

- Processed comparison datasets:
  - `artifacts/data/realistic-clean/bare-patator-cic.parquet`
  - `artifacts/data/realistic-clean/concap-patator-cic.parquet`
- Additional realism cross-check datasets:
  - `artifacts/data/realistic-clean/bare-nmap-cic.parquet`
  - `artifacts/data/realistic-clean/concap-nmap-cic.parquet`

The public release intentionally keeps the cleaned comparison artifacts and does
not redistribute raw packet captures or unsanitized flow exports.

## 6. What This Repository Does Not Cover

This repository is an HsP artifact bundle. It is not a full release of every
adjacent research asset.

Excluded from this public pass:

- third-party benchmark base datasets
- broader ConCap and SaTML workspaces
- reviewer-specific intermediate bundles
- raw packet captures and unsanitized real-world flow exports
