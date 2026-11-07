# HiSpoT — dual-barcode NGS spoligotyping of *Mycobacterium tuberculosis* complex

**HiSpoT: a novel one-tube dual-barcode PCR method for NGS spoligotyping amplicon library preparation in *Mycobacterium tuberculosis* complex**

HiSpoT (High-throughput Spoligotyping by Targeted next-generation sequencing) combines a one-tube dual-barcode PCR approach with open-source analysis of Illumina paired-end FASTQ data. The assay targets the classical 43-spacer CRISPR direct-repeat (DR) region used for spoligotyping of the *Mycobacterium tuberculosis* complex (MTBC). Its PCR-based outputs are designed to remain comparable with historical spoligotyping datasets.

## Research overview

In a study of 288 clinical MTBC isolates from Israel collected during 2020–2022, HiSpoT was used to characterize genetic lineages. Among 79 isolates assessed by both HiSpoT and whole-genome sequencing (WGS), full spoligotype concordance was reported for 70%; the manuscript attributes the discrepancies primarily to insertion-element disruptions affecting PCR primer sites at individual spacers.

The manuscript describes a dual-barcode primer approach for multiplexing up to 96 samples without a commercial NGS library-preparation kit. These laboratory-method claims relate to the accompanying research manuscript and should not be interpreted as independently validated software benchmarks.

## Software

This repository provides **both** software implementations described in the manuscript:

- **[Spoligotyping_MTBC_gcl](Spoligotyping_MTBC_gcl/)** — the original object-oriented Google Colab notebook developed by Paul J. Freidlin, with two Python modules and an Excel template in its `spo_software_modules_and_template_file/` subdirectory.
- **[`HiSpoT_Spoligotyping_v8_ready.ipynb`](HiSpoT_Spoligotyping_v8_ready.ipynb)** — the later VIBE-coded, condensed Google Colab implementation.

Both implementations are distributed under the repository MIT license (subject to third-party rights); see [LICENSING_AND_PERMISSIONS.md](LICENSING_AND_PERMISSIONS.md). The original OOP software was added after the historical `v8.0` tag and is therefore available on `main`, not in that release snapshot.

The analysis workflow is intended to process Illumina paired-end FASTQ reads from HiSpoT assays or WGS and generate, as supported by the notebook:

- Binary and octal 43-spacer spoligotype profiles
- Spoligotype international type (SIT) and MTBC family assignments
- Quality-control and analysis reports

**Important:** **SITVIT lookup limitation (intentional in v8.0):** The maintainer has chosen to distribute the existing *trimmed* SITVIT dictionary, rather than the full original dictionary. Consequently, an unmatched octal profile does **not** by itself establish a novel SIT or lineage. Confirm dictionary coverage and independently verify critical SIT/family assignments before publication or surveillance use. See [VALIDATION.md](VALIDATION.md) for the repository audit.

Assignment results depend on the reference databases and analysis logic embedded in or accessed by the notebook. Consult the notebook and the user manual for the exact behavior of version 8.

## Getting started

1. Open `HiSpoT_Spoligotyping_v8_ready.ipynb` in Google Colab.
2. Consult **`HiSpoT Spoligotyping v8 — User Manual.docx`** before running the workflow.
3. Prepare Illumina paired-end FASTQ inputs in the format described by the notebook and manual.
4. Follow the notebook's cells in their documented order, including any Google Drive authorization, database loading, or parameter selection required by the notebook.
5. Review the quality-control outputs before interpreting spoligotype, SIT, or family assignments.

The repository includes a `HiSpoT_fastq_files_for_validation/` directory intended for example/validation data. Confirm the contents, data-sharing permissions, and expected results before using them for formal benchmarking.

**Environment:** Google Colab / Python. The notebook installs `tqdm`, `openpyxl`, `ipyfilechooser`, and `pyahocorasick` (with a fallback scanner if the latter is unavailable); it also imports `pandas` and uses Colab's Google Drive integration. Exact dependency versions have not been pinned or independently tested.

**Outputs:** The notebook writes timestamped results under `MyDrive/HiSpoT_Fastq/`, including `clinical_spoligotyping_results.xlsx` and `.txt`.

## Scope and limitations

Spoligotyping is useful for continuity with historical typing databases and for epidemiological screening, but it has lower discriminatory resolution than WGS. HiSpoT results should be interpreted alongside epidemiological and, where appropriate, WGS evidence. The study's reported 70% full agreement in the paired-method comparison should be considered when selecting a typing strategy.

This repository is a research tool, not a standalone clinical diagnostic device. Users are responsible for validation in their own setting and for protecting patient-associated sequence data.

## Authors

1. Paul J. Freidlin (1, 2)
2. Mor Rubinstein (1)
3. Ephraim Fass (1)
4. Inna Kutikov (1)
5. Gal Zizelski Valenci (1)
6. Yelena Losev (1)
7. Zeev Dveyrin (1)
8. Efrat Rorman (1)
9. Israel Nissan (1, 2; corresponding author)

**(1)** National Public Health Laboratory, Public Health Directorate, Ministry of Health, Tel Aviv, Israel.  
**(2)** Department of Avian Diseases, Kimron Veterinary Institute, Ministry of Agriculture, Beit Degan, Israel.

**Correspondence:** Israel Nissan, PhD — israel.nissan@gmail.com

## Publication and citation

**Manuscript preprint (bioRxiv, posted 2026-11-05):** Freidlin, P. J., et al. *HiSpoT: a novel one-tube dual-barcode PCR method for NGS spoligotyping amplicon library preparation in Mycobacterium tuberculosis complex.* **DOI:** [10.1101/2026.11.04.764218](https://doi.org/10.1101/2026.11.04.764218). [Read the preprint PDF](https://www.biorxiv.org/content/biorxiv/early/2026/11/05/2026.11.04.764218.full.pdf).

**Software archive (Zenodo):** [10.5281/zenodo.23948119](https://doi.org/10.5281/zenodo.23948119). **GitHub release:** [HiSpoT v8.1 — Dual Software Release](https://github.com/isrulik67/HiSpoT-dual-barcode-NGS-spoligotyping-of-M.-tuberculosis/releases/tag/v8.1).

The bioRxiv DOI identifies the **manuscript**; the Zenodo DOI was supplied for the **software archive**. The Zenodo record's version-specific versus concept DOI status has not been independently verified here. Cite the software and manuscript separately. The bioRxiv posting is a preprint, not a peer-reviewed journal publication.

## License

See [`LICENSE`](LICENSE) for the repository's license terms. Check third-party datasets, reference databases, and software dependencies separately before redistribution.

## Keywords

Spoligotyping; *Mycobacterium tuberculosis* complex; next-generation sequencing; CRISPR; molecular epidemiology; HiSpoT; tuberculosis genotyping; spoligotyping software.
