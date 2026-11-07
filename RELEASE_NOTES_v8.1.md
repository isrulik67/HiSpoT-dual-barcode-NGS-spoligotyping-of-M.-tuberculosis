# HiSpoT v8.1 — Dual Software Release

## Two complementary MTBC spoligotyping analysis implementations

This release makes **both** open-source Google Colab analysis implementations described in the HiSpoT manuscript available in one citable source snapshot.

### Included software

**1. Spoligotyping_MTBC_gcl — original object-oriented implementation**
- Original developer: **Paul J. Freidlin**.
- Notebook: `Spoligotyping_MTBC_gcl/spoligotyping_MTBC_gcl_ver01.ipynb`.
- Supporting modules and Excel template: `Spoligotyping_MTBC_gcl/spo_software_modules_and_template_file/`.
- Follow the dedicated [setup README](Spoligotyping_MTBC_gcl/README.md). In Google Drive, the support folder is expected under `MyDrive/data/`. The original code contains some hard-coded Drive paths, as documented.

**2. HiSpoT_Spoligotyping_v8_ready — later VIBE-coded implementation**
- Notebook: `HiSpoT_Spoligotyping_v8_ready.ipynb`.
- Supports HiSpoT amplicon and WGS FASTQ analysis, binary and octal spoligotypes, QC outputs, and SIT/family lookup where covered by the bundled reference.

### Versioning and reproducibility
- **v8.1 is a combined distribution release**, not a claim of a new analysis algorithm.
- The source code of both implementations is preserved unchanged during packaging and repository reorganization.
- The prior **v8.0** release remains an unchanged historical snapshot.
- The maintainer reports repeated successful runs of the v8 notebook in Google Colab. Independent execution of the original object-oriented package has not been performed as part of this repository audit.

### Important limitations
- The v8 notebook intentionally uses a **trimmed SITVIT dictionary**; unmatched profiles are not necessarily novel.
- The original OOP notebook expects specific Google Drive folders and FASTQ naming conventions. Review its README and validation checklist before use.
- External reference databases, datasets and dependencies may have their own terms.

### License and attribution
Both project-owned software implementations are distributed under **MIT**; see `LICENSE` and `LICENSING_AND_PERMISSIONS.md`. Preserve original copyright notices. Credit Paul J. Freidlin for the original OOP implementation. See `CITATION.cff` for citation metadata. Software Zenodo DOI: [10.5281/zenodo.23948119](https://doi.org/10.5281/zenodo.23948119) (version-specific versus concept DOI status not independently verified).

### Publication
This release accompanies the manuscript **“HiSpoT: a novel one-tube dual-barcode PCR method for NGS spoligotyping amplicon library preparation in Mycobacterium tuberculosis complex.”** The manuscript is available as a **bioRxiv preprint** (posted 2026-11-05): DOI [10.64898/2026.11.04.764218](https://doi.org/10.64898/2026.11.04.764218); [full PDF](https://www.biorxiv.org/content/biorxiv/early/2026/11/05/2026.11.04.764218.full.pdf). This is the **manuscript DOI**, not the software DOI. The bioRxiv posting is a preprint, not a peer-reviewed journal publication.
