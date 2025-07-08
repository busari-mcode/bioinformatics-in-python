# DNA Toolset/Code testing file
from DNAToolkit import *
import random

# Creating a random DNA Sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

print(validateSeq(randDNAStr))
print(countNucFrequency(randDNAStr))


# ************************ LEARNING PHASE 1 ******************************
# ****************Validate DNA Sequence*************

# # DNA Toolset/Code testing file
# from DNAToolkit import *

# # random DNA string
# rndDNAStr = "ATTTCGT"
# rndDNAStr2 = "ATTTCGTX"
# rndDNAStr3 = "AtCCgGGtGGt"

# print(validateSeq(rndDNAStr))
# print(validateSeq(rndDNAStr2))
# print(validateSeq(rndDNAStr3))
