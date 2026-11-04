# HiSpoT v8.0 — pre-release verification record

This document records a **static source inspection** of `HiSpoT_Spoligotyping_v8_ready.ipynb`. It is not an execution test or independent validation of scientific performance.

## Confirmed in the notebook source

- Google Colab workflow with Google Drive mounting and an interactive FASTQ folder chooser.
- Modes: `auto`, `HiSpoT` (amplicon), and `WGS`; read layout `auto`, `paired`, or `single`.
- FASTQ discovery supports `.fastq`/`.fq` and gzipped forms with multiple mate-naming conventions.
- Parameters include amplicon threshold, minimum reads, WGS coverage-aware calling, auto-mode selection, and QC thresholds.
- The notebook installs `tqdm`, `openpyxl`, `ipyfilechooser`, and `pyahocorasick` (with a pure-Python scanner fallback); `pandas` is imported.
- Results are saved to timestamped folders under `/content/drive/MyDrive/HiSpoT_Fastq/`, including `clinical_spoligotyping_results.xlsx` and `.txt`.
- The notebook explicitly labels the embedded SITVIT dictionary **“trimmed to save space – full dict in original code.”**

## Scientific release blocker: reference-dictionary coverage

The current notebook embeds a reduced SITVIT octal-to-SIT/family lookup dictionary. A valid binary/octal spoligotype can therefore lack an SIT/family assignment simply because its entry is absent. **Do not interpret an unassigned profile as a novel spoligotype or a new lineage without checking against a complete, curated reference.**

**Maintainer decision (2026-11-04):** Release v8.0 with the existing **trimmed SITVIT dictionary**. Do not restore or expand the reference dictionary for this release. Missing SIT/family assignments may reflect limited dictionary coverage, not novel biological profiles. This decision does not replace the remaining execution and data-sharing checks.

## Maintainer-reported runtime validation

The maintainer reports that the HiSpoT v8 notebook has been successfully tested multiple times in Google Colab. This is a **maintainer-reported validation**, not an independently reproduced execution in this repository audit. Run logs, expected-output fixtures, and environment snapshots have not been supplied for independent verification.

## Still requiring verification

- Independent reproduction of an end-to-end run in a fresh Google Colab runtime (maintainer reports multiple successful Colab runs).
- Availability and privacy/licensing review of example FASTQ files.
- Reproduction of expected binary, octal, SIT, family, and QC results on reference samples.
- Agreement of the user manual with the current v8 notebook and parameters.
- Verification of dependency compatibility and any third-party database redistribution rights.
- Addition of final journal/DOI metadata when available (not required for an initial software release).
- Confirmation that the intended v8.0 tag points to the reviewed notebook and documentation commit.

## Release decision

**Maintainer-reported Colab validation completed; independent verification and data-sharing review remain open.** No claim of independently reproduced benchmarks, DOI assignment, or GitHub Release creation is made here.
