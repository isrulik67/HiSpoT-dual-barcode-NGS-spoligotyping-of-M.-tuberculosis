# -*- coding: utf-8 -*-

# module: call_oligo_search_methods_ver1_2.py
# classes included in this module to date:
# 1) CallAndRunSpoligoMtbc
# search methods included in this module to date:
# 1) spo_mtbc_srch_algorithm

global My_project


class CallAndRunSpoligoMtbc:

    # ====================================================================================================
    # declare the variable types, lists, arrays, and global designations for the class within the methods
    # ====================================================================================================

    def __init__(self, number_of_samples, cutoff_parameter, assay_id, operator_name, my_project_crispr):
        self.number_of_samples = number_of_samples
        self.cutoff_parameter = cutoff_parameter
        self.assay_id = assay_id
        self.operator_name = operator_name
        self.my_project_crispr = my_project_crispr

    def spo_mtbc_srch_algorithm(self):

        #import numpy as np
        print("\n")

        print("the software Spoligotyping_MTBC_gcl including the Colab Notebook and all associated files (except for")
        print("AI assisted decompression of NGS output) were prepared and written by Dr. Paul Jeffrey Freidlin, Ph.D.")
        print("and copyright (C) 2026 by the Government of the State of Israel under applicable MIT license", "\n")
        print("call_oligo_search_methods_ver1_2_gcl.py (C) 2026 Government of the State of Israel, MIT license", "\n")
        print("HiSpoT (R) is a novel one-tube dual-barcode PCR-based cost efficient, high throughput,")
        print("targeted NGS technique developed by Dr. Israel Nissan, Ph.D. and his team.", " \n")
        print("SIT and family/clade values were sourced from Suppl-Table-S1-SITVITWEB.pdf of Dec 1,2016.", " \n")

        # answer1 = input(r"Shall we start spoligotyping? Press enter to start..., or type the word 'no' to quit  ")
        # if answer1 == "no":
        #     exit()
        # print("\n")

        # number_samples = np.int8(input("Number of samples (should be half the total number of files): "))
        # print("number_samples = ", number_samples)
        # print("\n")

        # cutoff_parameter = np.float32(input("Cutoff_parameter (try between 0.05 to 0.5, recommended initial 0.365):"))

        cutoff_parameter = self.cutoff_parameter
        print("cutoff_parameter = ", cutoff_parameter, "\n")
        if cutoff_parameter < 0.05:
            print("ERROR: cutoff_parameter should be between 0.05 to 0.5, recommended 0.365 WGS, 0.15 HiSpoT")
            exit()
        elif cutoff_parameter > 0.5:
            print("ERROR: cutoff_parameter should be between 0.05 to 0.5, recommended 0.365 WGS, 0.15 HiSpoT")
            exit()
        elif cutoff_parameter == str:
            print("ERROR: cutoff_parameter should be a number between 0.05 to 0.5, recommended 0.365 WGS, 0.15 HiSpoT")
            exit()

        # assay_id = str(input("assay_id (give name of 16 or less spaces and characters): "))
        assay_id = self.assay_id
        print("assay_id = ", assay_id, "\n")
        if len(assay_id) > 25:
            print("ERROR: assay_id name should be less than 26 spaces and characters:")
            exit()
        elif len(assay_id) < 1:
            print("ERROR: assay_id name should be at least 1 character, but less than 17 spaces and characters:")
            exit()

        # operator_name = str(input("operator_name is (give name of 16 or less spaces and characters): "))
        operator_name = self.operator_name
        print("operator_name = ", operator_name, "\n")
        if len(operator_name) > 25:
            print("ERROR: assay_id name should be less than 26 spaces and characters:")
            exit()
        elif len(operator_name) < 1:
            print("ERROR: assay_id name should be at least 1 character, but less than 17 spaces and characters:")
            exit()

        print("For transformation from number of matches per spacer, to binary 0 or 1 for each spacer:")
        print("the cutoff is calculated as mean number of matches (meanarr) * cutoff_parameter, to decide whether")
        print("the number of matches for a given spacer should be represented as negative [0] or positive [1].")
        print("Less than 10 matches for any given spacer is automatically designated as negative [0]")
        print("\n")
        # answer2 = input("Shall we continue spoligotyping? Press enter to continue..., or type the word 'no' to quit ")
        # if answer2 == "no":
        #     exit()

        # Below are attributes to be passed to class SpoligoMtbc located in cris (the module crispr_search_ver1_1_gcl)
        # Note: the module crispr_search_ver1_1_gcl was imported already as cris in the colab environment, but needs
        # to be imported again in this module.

        title_strings = "spacer oligonucleotide search within Mycobacterium tuberculosis bacteria complex"
        list_of_file_names = "list_of_file_names.txt"
        number_of_samples = self.number_of_samples  # inputted as "np.int8"
        cutoff_parameter = self.cutoff_parameter  # inputted as "np.float32"
        assay_id = self.assay_id
        operator_name = self.operator_name
        my_project_crispr = self.my_project_crispr

        # Note: the module "crispr_search_ver1_1_gcl" has already been imported in the Colab notebook
        import sys
        import os
        # Add the directory containing the module to the Python path
        sys.path.append(f'/content/drive/MyDrive/data/{my_project_crispr}')
        # Import the module
        try:
            import crispr_search_ver1_1_gcl as cris
            print("\n Module 'crispr_search_ver1_1_gcl' imported successfully.")
        except ModuleNotFoundError:
            print("\n Error: Module 'crispr_search_ver1_1_gcl' not found.")
            print("Please ensure the file 'crispr_search_ver1_1_gcl.py' exists in the directory")
            print(f'/content/drive/MyDrive/data/{my_project_crispr} and the filename is spelled correctly.')
        #
        #
        global sit_fam

        # creates an object of the class SpoligoMtbc with attribute arguments
        objspomtbc = cris.SpoligoMtbc(title_strings, list_of_file_names, number_of_samples, cutoff_parameter,
            assay_id, operator_name, my_project_crispr)

        # creates an instance of the object with method class_header
        objspomtbc.class_header()   # an object of the class can access any method (function) in the class

        # retrieves sample file names from a text file list, as instance of the object with method get_sample_file_names
        # allocates each data file to a list element of lstdfarray[] indices 0 through number of file names eg [191
        # (for a total of 192 files)]
        objspomtbc.get_sample_file_names()  # **** also contains initialized global variables

        # ###=================================================================================
        # INITIALIZE LISTS: SAMPLE DATAFILE NAMES, SPACER COUNTERS, F AND COMP REV F SPOLIGOS,
        # ###=================================================================================

        # initialize the values of the spacer counter (spactr) list of elements spactr[0] through spactr[42] to 0
        objspomtbc.init_each_spacercounter_list_element_to_equal_zero()

        # test to see that the spacer counter list spactr is global (available to all methods)
        # objspomtbc.test_of_global_spactr()  #diagnostic

        # get lists of forward (fsp) and complementary reverse (crsp) spacer oligonucleotides for class SpoligMTBC
        objspomtbc.lists_of_spoligomtbc_spacer_oligos()

        objspomtbc.get_read_search_extract_sample_data_files()

        objspomtbc.translate_runarr_spoligo_matches_into_01_binary()

        objspomtbc.translate_from_binary_to_octal()

        objspomtbc.print_notice_that_Spoligotyping_MTBC_gcl_run_completed()





# spo_mtbc_srch_algorithm():  this definition is now contained in a class, to be instantiated in an external class,

# and its functions used as object methods
