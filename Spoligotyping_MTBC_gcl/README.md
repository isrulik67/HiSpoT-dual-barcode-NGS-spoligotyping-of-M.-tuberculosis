# Spoligotyping_MTBC_gcl — object-oriented Google Colab implementation

This is the original object-oriented spoligotyping analysis implementation by **Paul J. Freidlin**, supplied alongside the later VIBE-coded **HiSpoT_Spoligotyping_v8_ready** notebook. Both implementations are discussed in the associated HiSpoT manuscript.

## Files

- `spoligotyping_MTBC_gcl_ver01.ipynb`: original Colab notebook.
- `spo_software_modules_and_template_file/call_oligo_search_methods_ver1_2_gcl.py`: object-oriented orchestration/search module.
- `spo_software_modules_and_template_file/crispr_search_ver1_1_gcl.py`: CRISPR spacer analysis module.
- `spo_software_modules_and_template_file/clinical_lab_results.xlsx`: Excel template.

## Setup (as described in the original notebook)

1. Mount Google Drive in Colab.
2. Create `MyDrive/data/` and place the entire `spo_software_modules_and_template_file` folder inside it.
3. Create a project folder under `MyDrive/data/`, and place the Illumina paired-end sequencing files in it.
4. Open the notebook in Colab and execute the cells in order. The original notebook requires paired FASTQ filenames containing `_R1` and `_R2`.
5. Verify the output with the author's reference data before analyzing new samples.

## Important limitations and provenance

- The source code is **unmodified** from the user-provided files. This package has not been independently executed in Colab.
- `crispr_search_ver1_1_gcl.py` contains hard-coded writes to `/content/drive/My Drive/data/HiSpoT/`; this may require the `HiSpoT` folder to exist and may conflict with a differently named project folder. Inspect this before use.
- The notebook says it was validated using Python 3.12.12; compatibility with other versions is not established here.
- **License: MIT.** The maintainer confirmed the uniform MIT license for both software implementations on 2026-11-04. The original notebook still contains a legacy CC BY-NC reference, preserved as historical source text; see `LICENSING_AND_PERMISSIONS.md`. Third-party dependencies and reference data retain their own terms.
- No patient data are included in this package. Example FASTQ validation data are not included in these two uploaded source files.
- SIT/family mapping and reference-database provenance should be evaluated separately from the v8 notebook's deliberately trimmed SITVIT dictionary.

## Citation

Cite the associated HiSpoT manuscript when published, and credit the original software authorship to Paul J. Freidlin. The bibliographic details and DOI have not yet been assigned.
