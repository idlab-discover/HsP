# Provenance Audit

This note records which local notebooks and result files appear to back the
final paper submissions in:

- `/Users/strgenix/Downloads/asiaccs2026b-final83.pdf`
- `/Users/strgenix/Downloads/satml-202626-paper46.pdf`

The goal is not to restate the papers. The goal is to track which local
artifacts actually line up with the published numbers, and where the current
repository curation is still incomplete.

## Current conclusions

- The current `artifacts/ml-evaluation/...latest` bundle is not sufficient to
  justify all final paper numbers.
- The older `cns22` lineage is still paper-critical for AsiaCCS.
- The legacy `ML/` workspace is still paper-critical for SaTML.
- Several published numbers are present only in notebook display outputs, not
  in clean exported summary files.

## AsiaCCS 2026

### Clean mappings

- Table 4 maps cleanly to:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point3_deep_ood/results/summary.json`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point3_deep_ood/results/guided_exemplar_summary.json`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point3_deep_ood/README.md`

- Table 5 maps cleanly to:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point7_non_ssh_hsp/results/baseline_results.csv`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point7_non_ssh_hsp/results/hsp_results.csv`

- Table 6 maps cleanly to:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point1_aci_iot_2023/results/hydra_results.csv`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/_reviewer_b/point1_aci_iot_2023/results/slowloris_results.csv`

### Main-table lineage

- Table 1 does not line up with the `latest` result directories.
- The benchmark baseline rows are tied to the older `cns22` lineage under:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/results/cicids2017-cns22`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/results/csecicids2018-cns22`

- The exact final-paper values for the harder CICIDS17 row, including the
  `0.214` and `0.073` recalls, appear in notebook output inside:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/defense/cicids2017-cns22.ipynb`

- That means the current repo should not claim that exported CSVs alone fully
  support Table 1.

### Real-world table

- Table 2 is not yet pinned to one clean exported result directory.
- The underlying data is clearly in:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/data/clean`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/data/concap/patator-ssh`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/data/bare-metal/patator-ssh`
- But I have not yet identified a single notebook or exported file that cleanly
  reproduces the final Table 2 values, including the `0.49` SVM case.

## SaTML 2026

### Clean mappings

- Tables I-III align with:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/realistic/README.md`

- The CVE packet and flow counts used in Table VI align with:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/data/new_dataset.ipynb`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/data/new-attacks/README.md`

- The corresponding CVE detection-result tables are exported under:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/results/cicids2017-cns22-all/adversarial-bis`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/results/cicids2018-cns22-all/adversarial-bis`

### Important caveats

- The local CVE result exports use `hist_gradient_boosting`, whereas the final
  paper tables refer to `XGB`. This needs explicit clarification before public
  release.
- Table VII training times appear in notebook outputs, but I have not yet found
  a clean exported summary file for them. Relevant workspaces are:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ML/defense-latest.ipynb`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ML/reversed_evaluation.ipynb`

### Still unresolved

- Table IV and Table V are not yet pinned to a single release-ready set of
  files.
- My current best guess is that they are split between:
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ml-evaluation/results/*cns22*`
  - `/Users/strgenix/postdoc/concap-full-dataset-creation/liechtenstein-usenix25/ML/reversed_evaluation.ipynb`
- This still needs a table-by-table confirmation pass.

## Implications for the public repo

- We should not ship only the `latest` notebooks and claim that they reproduce
  the final papers.
- We should include a provenance note for each paper table, especially where
  the authoritative values currently live only in notebook outputs.
- We likely need to export a few summary tables from notebooks into plain CSV or
  Markdown so the public artifact is auditable without opening Jupyter output.
- The legacy `ML/` tree cannot be dropped if we want a faithful SaTML artifact
  release.
