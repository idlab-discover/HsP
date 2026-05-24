# Artifact Map

This note maps the main HsP paper claims to the currently included repository artifacts.

It is a curation document, not a claim that every possible intermediate file from the original workspace belongs in the public release.

## 1. Core HsP Setup: `patator` SSH Variants

These files define the main SSH brute-force host-space perturbation families used throughout the paper.

- Scenarios:
  - `artifacts/scenarios/patator/`
- Cleaned flow artifacts:
  - `artifacts/data/concap-clean/patator-ssh-cic.parquet`
  - `artifacts/data/concap-clean/patator-ssh-cic-cns22.parquet`
  - `artifacts/data/concap-clean/patator-ssh-cic-nodelay.parquet`
  - `artifacts/data/concap-clean/patator-ssh-cic-nodelay-cns22.parquet`
  - `artifacts/data/concap-clean/patator-ssh-giovanni.parquet`

These are the main artifacts behind the `persistent=0` versus `persistent=1` HsP story.

## 2. Additional SSH HsP Families

These files support the paper's broader point that HsP are not restricted to one exact command string.

- Alternative SSH tool scenarios:
  - `artifacts/scenarios/hydra/`
  - `artifacts/scenarios/medusa/`
- Corresponding cleaned flow artifacts:
  - `artifacts/data/concap-clean/hydra-ssh-cic.parquet`
  - `artifacts/data/concap-clean/medusa-ssh-cic.parquet`

## 3. Network and Environment Variations

These files support the paper's discussion of perturbations that arise from network or environment changes rather than only command-flag changes.

- Network-condition scenarios:
  - `artifacts/scenarios/patator-network/`
- Environment/version scenarios:
  - `artifacts/scenarios/patator-versions/`
- Corresponding cleaned flow artifacts:
  - `artifacts/data/concap-clean/patator-network-ssh-cic.parquet`
  - `artifacts/data/concap-clean/patator-versions-ssh-cic.parquet`

## 4. Benchmark-Side ML Evidence

These files correspond to the latest curated notebooks and exported result tables for the benchmark experiments.

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

### Exported Results

- `artifacts/ml-evaluation/results/cicids2017-latest/baseline/`
- `artifacts/ml-evaluation/results/cicids2017-latest/generalisation/`
- `artifacts/ml-evaluation/results/cicids2017-latest/defense/`
- `artifacts/ml-evaluation/results/csecicids2018-latest/baseline/`
- `artifacts/ml-evaluation/results/csecicids2018-latest/generalisation/`
- `artifacts/ml-evaluation/results/csecicids2018-latest/defense/`

The CSV files in these directories are the most important public-facing artifacts because they expose the per-model outcomes without requiring the original workspace.

## 5. Real-World `patator` Comparison

These files support the paper's real-world network evidence for the SSH HsP claims.

### Cleaned Comparison Artifacts

- `artifacts/data/realistic-clean/bare-patator-cic.parquet`
- `artifacts/data/realistic-clean/concap-patator-cic.parquet`

### Raw Comparison Artifacts

- Bare-metal:
  - `artifacts/data/realistic-raw/patator-ssh/bare-metal/`
- ConCap:
  - `artifacts/data/realistic-raw/patator-ssh/concap/`

These directories currently include:

- `dump.pcap`
- `cicflowmeter.csv`
- `argus.csv`
- lightweight logs/configuration files

## 6. Realism Cross-Check Material

The repository currently also includes the cleaned `nmap` realism comparison artifacts:

- `artifacts/data/realistic-clean/bare-nmap-cic.parquet`
- `artifacts/data/realistic-clean/concap-nmap-cic.parquet`

These are not central to the HsP paper's SSH story, but they are small and useful as context for the realism claim.

## 7. Deliberate Omissions

The following areas were intentionally not brought into this first pass:

- `_reviewer_b/`
  - useful internally, but too revision-specific and too large for a first clean public release
- the older `ML/` tree
  - likely valuable for provenance, but not necessary in the first curated artifact bundle
- the broader ConCap workspace and SaTML artifact set
  - should be handled separately or linked out to `idlab-discover/ConCap`
- literature-review material
  - explicitly out of scope for the public HsP repository

## 8. Likely Next Curation Decisions

The next useful decisions for this repository are:

1. Whether to add a compact top-level `results-summary.md` with headline numbers extracted from the CSV files.
2. Whether to include selected figures only, or all exported confusion matrices and PDFs.
3. Whether to add a lightweight reproduction script that checks file presence and points users to the relevant notebooks.
4. Whether the post-acceptance non-SSH HsP material should live here or remain in a separate follow-up branch/repository.
