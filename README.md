# HsP

This repository is being prepared as the artifact repository for the ACM AsiaCCS 2026 paper:

`"What is the Problem Space?" Defining Host-space Adversarial Perturbations against Network Intrusion Detection Systems`

The current goal is not to mirror every file from the broader research workspace. The goal is to provide a clean, paper-focused repository containing:

- the SSH host-space perturbation scenarios used in the paper
- the processed flow artifacts used for the HsP experiments
- the latest benchmark, generalisation, and defense notebooks/results used for the paper narrative
- the real-world `patator` comparison artifacts used to support the host-space claims

## Status

This is an in-progress curation pass for the eventual public repository at:

- <https://github.com/idlab-discover/HsP>

The repository is intentionally being kept narrower than the earlier anonymous workspace:

- included: experimental artifacts directly tied to the HsP paper
- excluded for now: literature-review material, large reviewer-only recovery bundles, and broader ConCap/SaTML material not required to understand the HsP claims

## Repository Layout

```text
artifacts/
  data/
    concap-clean/              Cleaned ConCap flow datasets for SSH HsP families
    realistic-clean/           Cleaned bare-metal vs ConCap realism datasets
    realistic-raw/patator-ssh/ Real-world `patator` comparison captures and flow exports
  ml-evaluation/
    notebooks/                Curated notebooks for baseline, defense, and generalisation
    results/                  Exported result tables and confusion matrices
  scenarios/
    hydra/                    Alternative SSH tool scenarios
    medusa/                   Alternative SSH tool scenarios
    patator/                  Core `patator` SSH scenarios
    patator-network/          Network-condition perturbation scenarios
    patator-versions/         Tool/environment variation scenarios
docs/
  artifact-map.md             Mapping from paper claims/sections to repository artifacts
```

## Included In This First Curated Pass

- Core SSH HsP scenarios:
  - `artifacts/scenarios/patator`
  - `artifacts/scenarios/hydra`
  - `artifacts/scenarios/medusa`
  - `artifacts/scenarios/patator-network`
  - `artifacts/scenarios/patator-versions`
- Processed ConCap datasets:
  - `artifacts/data/concap-clean/*.parquet`
- Real-world comparison artifacts:
  - `artifacts/data/realistic-clean/*`
  - `artifacts/data/realistic-raw/patator-ssh/*`
- Latest ML evaluation notebooks and exported results for:
  - `CICIDS2017`
  - `CSE-CIC-IDS2018`
  - baseline
  - generalisation
  - defense

## Not Included Yet

- the broader reviewer-revision workspace under `_reviewer_b/`
- broader non-SSH HsP additions prepared after acceptance
- legacy duplicate notebooks under the older `ML/` tree
- benchmark source datasets themselves
- the full ConCap engine source tree

Those omissions are intentional for now. The immediate target is a clean HsP paper-artifacts repository, not a monorepo for every adjacent project.

## Benchmark Data

This repository includes processed HsP-specific artifacts, but it does not currently redistribute the underlying benchmark datasets. The notebooks and exported result files therefore serve as the main paper-facing evidence, while the benchmark base data should be obtained from its original sources.

## Provenance

The files currently in this repository were curated from the larger local research workspace used for the HsP and ConCap papers. This repository is meant to become the public-facing, paper-specific subset.

See [docs/artifact-map.md](docs/artifact-map.md) for the current mapping from paper content to included files.
