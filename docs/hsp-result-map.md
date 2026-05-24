# HsP Result Map

This note is narrower than [`docs/provenance-audit.md`](/Users/strgenix/postdoc/concap-full-dataset-creation/idlab-discover-hsp-repo/docs/provenance-audit.md:1).
Its purpose is simple: for each HsP-related result in the final AsiaCCS and
SaTML submissions, identify the best local source file to point to today, even
if that source is a notebook with stored outputs rather than a release-ready
CSV.

The source PDFs used for this mapping are:

- `/Users/strgenix/Downloads/asiaccs2026b-final83.pdf`
- `/Users/strgenix/Downloads/satml-202626-paper46.pdf`

## AsiaCCS 2026: HsP Paper

### Table 1: Benchmark HsP on CICIDS17 and CICIDS18

Best local sources:

- Primary notebooks:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/defense/cicids2017-cns22.ipynb`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/defense/csecicids2018-cns22.ipynb`
- Companion result trees:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/results/cicids2017-cns22`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/results/csecicids2018-cns22`

Why these:

- The final paper clearly uses the older `cns22` benchmark lineage, not the
  `latest` lineage.
- Some final-paper values are visible directly in notebook outputs and are not
  yet pinned to one compact export. In particular, the CICIDS17 row with
  `0.214` and `0.073` is present in
  `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/defense/cicids2017-cns22.ipynb`.

Working rule:

- If we need one file to justify a Table 1 number today, point to the relevant
  `cns22` defense notebook first.
- If we need the full per-model artifacts, point to the corresponding
  `ml-evaluation/results/*-cns22` directory.

### Table 2: Real-world HsP on `patator --persistent=0/1`

Best local sources:

- Cleaned real-world datasets:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/data/clean/bare-patator-cic.parquet`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/data/clean/concap-patator-cic.parquet`
- Dataset construction notebook:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/clean_flows.ipynb`
- Supporting overview:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/README.md`

Current limitation:

- I have not found a dedicated ML-evaluation notebook or exported result file
  that cleanly corresponds to the final Table 2 numbers, including the SVM
  `0.49` case, in the same way that Table 1 maps to the `cns22` notebooks.

Working rule:

- Today, Table 2 should be mapped to the `realistic` cleaned patator artifacts
  and their construction notebook, with an explicit note that the exact table
  values still need a later export pass.

### Table 3: Additional SSH HsP variants

Best local sources:

- Scenario inputs:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/scenarios/hydra`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/scenarios/medusa`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/scenarios/patator-network`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/scenarios/patator-versions`
- Cleaned flow artifacts:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/data/concap/clean/hydra-ssh-cic.parquet`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/data/concap/clean/medusa-ssh-cic.parquet`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/data/concap/clean/patator-network-ssh-cic.parquet`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/data/concap/clean/patator-versions-ssh-cic.parquet`

Note:

- Table 3 is in Appendix B of the paper rather than the main body, but it is
  still part of the HsP result set. I have not pinned it to one single summary
  notebook yet.

### Table 4: Additional DL-based classifiers

Best local sources:

- `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point3_deep_ood/results/summary.json`
- `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point3_deep_ood/results/guided_exemplar_summary.json`
- `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point3_deep_ood/README.md`

### Table 5: Non-SSH HsP

Best local sources:

- `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point7_non_ssh_hsp/results/baseline_results.csv`
- `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point7_non_ssh_hsp/results/hsp_results.csv`

### Table 6: Different benchmark / ACI-IoT follow-up

Best local sources:

- `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point1_aci_iot_2023/results/hydra_results.csv`
- `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point1_aci_iot_2023/results/slowloris_results.csv`

## SaTML 2026: ConCap Paper

This paper is broader than HsP. The table mapping below is therefore limited to
the pieces most directly tied to the HsP story and its prerequisites.

### Table IV: Reproducibility of prior work with `ssh-patator`

Best local sources:

- Primary notebook:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ML/reversed_evaluation.ipynb`
- Companion per-model result files:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ML/results/cicids2017`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ML/results/csecicids2018`

Why these:

- The notebook reads the older fixed benchmark datasets and
  `patator-ssh-cic-cns22.parquet`, which matches the paper's older benchmark
  lineage.
- The `ML/results/cicids2017` and `ML/results/csecicids2018` CSVs look like
  the on-disk outputs for the notebook's five-fold runs.

Working rule:

- Use `ML/reversed_evaluation.ipynb` as the best single provenance file for
  Table IV.
- Use the matching `ML/results/...` CSVs when we want the per-model mean rows
  without opening notebook output.

### Table V: Real-world equivalence

Best local sources:

- Real-world datasets:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/data/clean/bare-patator-cic.parquet`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/data/clean/concap-patator-cic.parquet`
- Dataset construction and comparison notebooks:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/clean_flows.ipynb`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/flow_stats_patator.ipynb`
- Supporting overview:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/README.md`

Current limitation:

- I have not yet identified a dedicated ML notebook or result export that
  materializes Table V itself. Unlike Table IV, this table currently maps most
  cleanly to the real-world patator datasets and the notebooks that build and
  analyze them.

Working rule:

- Treat the `realistic` patator bundle as the current provenance anchor for
  Table V, and plan a later pass to export the exact ML results into a small
  table.

### Table VII: Training times for the real-world-network assessment

Best local source:

- `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ML/defense-latest.ipynb`

Why this:

- The notebook has stored outputs containing `fit_time` summaries for the
  relevant train sets and models, and those outputs are the current closest
  match to the training-time table.

Note:

- Table VII is not itself an HsP result, but it is adjacent to the real-world
  HsP evaluation and may need to remain in scope if we later build one compact
  artifact index for the paper.

## Practical release implication

If we publish the current repo before reworking notebooks into compact tables,
the safest wording is:

- AsiaCCS Table 1 provenance lives in the `ml-evaluation/...cns22` notebooks
  and result trees.
- AsiaCCS Tables 4-6 map cleanly to reviewer-follow-up CSV/JSON files.
- SaTML Table IV maps to `ML/reversed_evaluation.ipynb` plus `ML/results/...`.
- The real-world patator tables in both papers currently map most directly to
  the `realistic` cleaned datasets and notebooks, not yet to a single compact
  result export.
