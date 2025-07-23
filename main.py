# DNA Toolset/Code testing file
from DNAToolkit import *
import random

# Creating a random DNA Sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)

print(f'\nSequence: {DNAStr}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')




# *************************************** LEARNING PHASE 3 *******************************************
# # DNA Toolset/Code testing file
# from DNAToolkit import *
# import random

# # Creating a random DNA Sequence for testing:
# randDNAStr = ''.join([random.choice(Nucleotides)
#                       for nuc in range(50)])

# DNAStr = validateSeq(randDNAStr)
# print(countNucFrequency(DNAStr))
# print(transcription(DNAStr))



# *************************************** LEARNING PHASE 2 *******************************************
# ****************Counting Nucleotides in the Validated random DNA String generated*************

# # DNA Toolset/Code testing file
# from DNAToolkit import *
# import random

# # Creating a random DNA Sequence for testing:
# randDNAStr = ''.join([random.choice(Nucleotides)
#                       for nuc in range(50)])

# DNAStr = validateSeq(randDNAStr)
# print(countNucFrequency(DNAStr))


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
