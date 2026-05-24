# HsP

This repository contains the public artifact bundle for the ACM AsiaCCS 2026
paper:

`"What is the Problem Space?" Defining Host-space Adversarial Perturbations against Network Intrusion Detection Systems`

The repository is intentionally narrow. It focuses on the SSH host-space
perturbation artifact set used to study how attacker-side execution changes can
shift network-flow behavior and downstream IDS performance.

## Scope

The public release includes:

- scenario definitions for the SSH HsP families discussed in the paper
- processed parquet datasets used for the curated HsP comparisons
- exported ML evaluation outputs for baseline, generalisation, and defense runs
- cleaned real-world comparison artifacts for the bare-metal versus ConCap SSH
  assessment

The public release does not attempt to mirror the full internal research
workspace. In particular, it does not redistribute:

- third-party benchmark base datasets
- broader ConCap or SaTML workspaces
- reviewer-specific intermediate material
- raw packet captures and unsanitized flow exports from the real-world runs

## Repository Layout

```text
artifacts/
  data/
    concap-clean/              Processed ConCap flow datasets for SSH HsP families
    realistic-clean/           Processed bare-metal vs ConCap comparison datasets
    realistic-raw/             Placeholder note for omitted raw capture material
  ml-evaluation/
    notebooks/                Curated notebooks for baseline, defense, and generalisation
    results/                  Exported result tables and figures
  scenarios/
    hydra/                    Alternative SSH tool scenarios
    medusa/                   Alternative SSH tool scenarios
    patator/                  Core `patator` SSH scenarios
    patator-network/          Network-condition perturbation scenarios
    patator-versions/         Tool/environment variation scenarios
docs/
  artifact-map.md             Mapping from paper topics to repository artifacts
  reproducibility.md          How to audit and reuse the public bundle
  results-summary.md          High-level summary of the included experiment bundles
scripts/
  check_artifacts.py          Lightweight release-integrity check
```

## Included Artifact Families

- `artifacts/scenarios/`
  - 47 YAML scenario definitions across `patator`, `hydra`, `medusa`,
    `patator-network`, and `patator-versions`
- `artifacts/data/concap-clean/`
  - 9 processed parquet datasets covering the SSH HsP families
- `artifacts/data/realistic-clean/`
  - 4 processed parquet datasets for the bare-metal versus ConCap comparison
- `artifacts/ml-evaluation/notebooks/`
  - 6 curated notebooks spanning `CICIDS2017` and `CSE-CIC-IDS2018`
- `artifacts/ml-evaluation/results/`
  - 6 exported result bundles
  - 78 per-model CSV result files, plus confusion matrices and serialized model
    outputs

Representative files:

- `artifacts/scenarios/patator/patator_ssh_cic_T10_P.yaml`
- `artifacts/data/concap-clean/patator-ssh-cic.parquet`
- `artifacts/data/realistic-clean/bare-patator-cic.parquet`
- `artifacts/ml-evaluation/results/cicids2017-latest/defense/support_vector_machine_results.csv`

## Reproducibility Notes

This repository is a curated artifact release, not a one-command rebuild of the
entire experimental workspace.

- The exported CSV files under `artifacts/ml-evaluation/results/` are the main
  paper-facing evidence in this public bundle.
- The notebooks document the evaluation workflow, but rerunning them requires
  separately obtaining the underlying benchmark datasets from their original
  sources.
- The cleaned parquet files in `artifacts/data/` can be inspected directly
  without access to the original packet captures.

See [docs/reproducibility.md](docs/reproducibility.md) for the public audit and
reuse guidance, and [docs/artifact-map.md](docs/artifact-map.md) for the
artifact-to-topic mapping.
