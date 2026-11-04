# HiSpoT v8.0 — GitHub Release Notes (draft)

## HiSpoT: dual-barcode NGS spoligotyping of *Mycobacterium tuberculosis* complex

This release packages the existing HiSpoT v8 Google Colab analysis notebook for research use alongside documentation, example FASTQ files, and software citation metadata.

### Highlights
- Analysis of HiSpoT amplicon and WGS FASTQ data using assay-aware spacer calling.
- Automatic, paired-end, and single-end read-layout options.
- Support for common FASTQ naming patterns and gzip-compressed reads.
- Binary and octal spoligotypes, SIT and family lookup where covered by the bundled dictionary, and quality-control outputs.
- Excel and tab-separated text result exports.
- Aho-Corasick scanner with pure-Python fallback.
- Google Colab workflow with Google Drive input selection.

### Important reference limitation
The embedded SITVIT lookup dictionary is **intentionally a trimmed subset**. Missing SIT or family assignments can reflect absent dictionary entries and must not be interpreted as proof of a new spoligotype or lineage. Binary and octal profiles should be checked against a complete curated reference when required.

### Validation and example data
The maintainer reports repeated successful runs in Google Colab and confirms that the repository's example FASTQ files contain no patient information. These statements are maintainer-reported; no independent benchmark reproduction or redistribution-rights audit is claimed.

### Getting started
Open `HiSpoT_Spoligotyping_v8_ready.ipynb` in Google Colab and follow `HiSpoT Spoligotyping v8 — User Manual.docx`. The notebook writes timestamped results to Google Drive under `HiSpoT_Fastq/`.

### Citation
Please use `CITATION.cff` for the nine-author software citation. Journal citation details and a DOI may be added after publication or archival deposition.

### Code stability
The v8 analysis notebook and underlying algorithm have not been modified as part of this documentation/release-preparation work.

**Status:** Release notes prepared. A GitHub Release/tag and Zenodo DOI have not yet been created.
