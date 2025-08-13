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

    # # Pythonic approach. A little bit faster solution.
    # mapping = str.maketrans('ATCG', 'TAGC')
    # return seq.translate(mapping)[::-1]

def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round((seq.count('C') * seq.count('G')) / len(seq) * 100)

def gc_content_subsec(seq, k=20):
    """GC Content in a DNA/RNA sub-sequence length k, k=20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res

def translate_seq(seq, init_pos=0):
    """Translates a DNA Sequence into an aminoacid sequence"""
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]

def codon_usage(seq, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(collections.Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict


# *************************************** LEARNING PHASE 4 *******************************************
# DNAStr = 'ATCGTAGGTTACGTATATTTAGATAC'
# txtStr = "He kept walking and walking and walking through the rain and the wind and the dark thinking and thinking and thinking about everything and nothing and everything again as the world spun and spun and spun around him without pause without mercy without end"

# print(DNAStr[::-1])
# print(txtStr.split(' '))

# wordCountDict = {}

# for word in txtStr:
#     if word in wordCountDict:
#         wordCountDict[word] += 1
#     else:
#         wordCountDict[word] = 1
# print(wordCountDict)

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