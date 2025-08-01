def countNucFrequency(seq):
    """counting nucleotide frequency"""
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

DNAString = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
result = countNucFrequency(DNAString)
print(result)
print(' '.join([str(val) for key, val in result.items()]))