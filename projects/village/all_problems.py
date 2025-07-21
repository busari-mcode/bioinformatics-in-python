#********************* Dictionaries *******************
# # method 1
# txtStr = 'We tried list and we tried dicts also we tried Zen'

# # Generic approach:
# wordCountDict = {}

# for word in txtStr.split(' '):
#     if word in wordCountDict:
#         wordCountDict[word] += 1
#     else:
#         wordCountDict[word] = 1

# for key, value in wordCountDict.items():
#     print(key, value)


# method 2
# # optimized pythonic approach using collections module
# from collections import Counter

# txtStr = 'We tried list and we tried dicts also we tried Zen'

# wordCountDict = Counter(txtStr.split(' '))

# for key, value in wordCountDict.items():
#     print(key, value)


#********************* Working with Files *******************
# outputFile = []

# with open('projects/village/input.txt', 'r') as f:
#     outputFile = [line for pos, line in enumerate(
#         f.readlines()) if pos % 2 != 0]

# print(outputFile) # just to confirm that previous code works

# # this will create a new file 'output.txt' with content in it
# with open('projects/village/output.txt', 'w') as f:
#     f.write(''.join([line for line in outputFile]))


#********************* Conditions and Loops *******************
# add all the odd integers from 100 to 200

# # method 1
# startPos = 100
# endPos = 200
# result = 0

# for x in range(startPos, endPos + 1):
#     if x % 2 != 0:
#         result += x
# print(result)

# # method 2
# startPos = 100
# endPos = 200

# numbList = [x for x in range(startPos, endPos + 1) if x % 2 != 0]
# result = sum([x for x in range(startPos, endPos + 1) if x % 2 != 0])

# print(numbList)
# print(result)


# ********* Strings and Lists ************
# wordOneStartPos = 22
# wordOneEndPos = 27

# wordTwoStartPos = 97
# wordTwoEndPos = 102

# txtStr = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"

#         # Note: end position is not inclusive, so we add 1 to capture it
# print(
#     f'{txtStr[wordOneStartPos:wordOneEndPos + 1]} {txtStr[wordTwoStartPos:wordTwoEndPos + 1]}'
# )
