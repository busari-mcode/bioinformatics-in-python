# DNA Toolkit file
import collections
# from structures file, import everything
from structures import *

# Check the sequence to make sure it is a DNA String
def validateSeq(dna_seq):
    """validating sequence for DNA string"""
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    """counting nucleotide frequency"""
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

    # the four lines of codes above can be replaced by the line below here 
    # using the collection module
    # return dict(collections.Counter(seq))

def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracial"""
    return seq.replace("T", "U")

def reverse_complement(seq):
    """"Swapping adenine with thymine and guanine wiht cytosine. Reversing newly generated string"""
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]








# *************************************** LEARNING PHASE 2 *******************************************
# ****************Counting Nucleotides in the Validated random DNA String generated*************

# # DNA Toolkit file
# import collections

# Nucleotides = ["A", "C", "G", "T"]

# # Check the sequence to make sure it is a DNA String
# def validateSeq(dna_seq):
#     tmpseq = dna_seq.upper()
#     for nuc in tmpseq:
#         if nuc not in Nucleotides:
#             return False
#     return tmpseq


# def countNucFrequency(seq):
#     tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
#     for nuc in seq:
#         tmpFreqDict[nuc] += 1
#     return tmpFreqDict

#     # the four lines of codes above can be replaced by the line below here 
#     # using the collection module
#     # return dict(collections.Counter(seq))



# ************************ LEARNING PHASE 1 ******************************
# ****************Validate DNA Sequence*************

# # DNA Toolkit file

# Nucleotides = ["A", "C", "G", "T"]

# # Check the sequence to make sure it is a DNA String
# def validateSeq(dna_seq):
#     tmpseq = dna_seq.upper()
#     for nuc in tmpseq:
#         if nuc not in Nucleotides:
#             return False
#     return tmpseq