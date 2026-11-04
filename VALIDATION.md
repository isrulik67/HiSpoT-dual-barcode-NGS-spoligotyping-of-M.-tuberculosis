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

Before archival publication, decide whether to (a) restore the complete authorized dictionary and validate assignments, or (b) clearly release the subset as a documented limitation. Any dictionary update should be separately versioned and validated; the notebook was not modified during this documentation pass.

## Still requiring verification

- End-to-end execution in a fresh Google Colab runtime.
- Availability and privacy/licensing review of example FASTQ files.
- Reproduction of expected binary, octal, SIT, family, and QC results on reference samples.
- Agreement of the user manual with the current v8 notebook and parameters.
- Verification of dependency compatibility and any third-party database redistribution rights.
- Confirmation of the manuscript author list and final publication metadata before archiving.
- Confirmation that the intended v8.0 tag points to the reviewed notebook and documentation commit.

## Release decision

**Not yet independently validated for archival release.** Documentation preparation is complete in part; the items above remain open. No claim of successful execution, benchmark reproduction, DOI assignment, or GitHub Release creation is made here.
