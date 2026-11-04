# HiSpoT — dual-barcode NGS spoligotyping of *Mycobacterium tuberculosis* complex

**HiSpoT: a novel one-tube dual-barcode PCR method for NGS spoligotyping amplicon library preparation in *Mycobacterium tuberculosis* complex**

HiSpoT (High-throughput Spoligotyping by Targeted next-generation sequencing) combines a one-tube dual-barcode PCR approach with open-source analysis of Illumina paired-end FASTQ data. The assay targets the classical 43-spacer CRISPR direct-repeat (DR) region used for spoligotyping of the *Mycobacterium tuberculosis* complex (MTBC). Its PCR-based outputs are designed to remain comparable with historical spoligotyping datasets.

## Research overview

In a study of 288 clinical MTBC isolates from Israel collected during 2020–2022, HiSpoT was used to characterize genetic lineages. Among 79 isolates assessed by both HiSpoT and whole-genome sequencing (WGS), full spoligotype concordance was reported for 70%; the manuscript attributes the discrepancies primarily to insertion-element disruptions affecting PCR primer sites at individual spacers.

The manuscript describes a dual-barcode primer approach for multiplexing up to 96 samples without a commercial NGS library-preparation kit. These laboratory-method claims relate to the accompanying research manuscript and should not be interpreted as independently validated software benchmarks.

## Software

This repository contains the Google Colab notebook **`HiSpoT_Spoligotyping_v8_ready.ipynb`**, the condensed HiSpoT v8 analysis workflow. The accompanying manuscript also describes **Spoligotyping_MTBC_gcl**, a separate analysis tool; its availability in this repository should not be assumed.

The analysis workflow is intended to process Illumina paired-end FASTQ reads from HiSpoT assays or WGS and generate, as supported by the notebook:

- Binary and octal 43-spacer spoligotype profiles
- Spoligotype international type (SIT) and MTBC family assignments
- Quality-control and analysis reports

**Important:** Assignment results depend on the reference databases and analysis logic embedded in or accessed by the notebook. Consult the notebook and the user manual for the exact behavior of version 8.

## Getting started

1. Open `HiSpoT_Spoligotyping_v8_ready.ipynb` in Google Colab.
2. Consult **`HiSpoT Spoligotyping v8 — User Manual.docx`** before running the workflow.
3. Prepare Illumina paired-end FASTQ inputs in the format described by the notebook and manual.
4. Follow the notebook's cells in their documented order, including any Google Drive authorization, database loading, or parameter selection required by the notebook.
5. Review the quality-control outputs before interpreting spoligotype, SIT, or family assignments.

The repository includes a `HiSpoT_fastq_files_for_validation/` directory intended for example/validation data. Confirm the contents, data-sharing permissions, and expected results before using them for formal benchmarking.

**Environment:** Google Colab / Python. Exact dependency versions and runtime requirements have not yet been independently verified; use the notebook's documented setup rather than assuming specific package versions.

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

## Citation

Please cite the accompanying manuscript when its bibliographic details become available. Until then, cite the software repository using the metadata in [`CITATION.cff`](CITATION.cff). A journal, DOI, or manuscript publication date has not yet been assigned in this repository's citation metadata.

## License

See [`LICENSE`](LICENSE) for the repository's license terms. Check third-party datasets, reference databases, and software dependencies separately before redistribution.

## Keywords

Spoligotyping; *Mycobacterium tuberculosis* complex; next-generation sequencing; CRISPR; molecular epidemiology; HiSpoT; tuberculosis genotyping; spoligotyping software.
