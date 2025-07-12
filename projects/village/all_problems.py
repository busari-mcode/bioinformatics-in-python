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

# method 2
startPos = 100
endPos = 200

numbList = [x for x in range(startPos, endPos + 1) if x % 2 != 0]
result = sum([x for x in range(startPos, endPos + 1) if x % 2 != 0])

print(numbList)
print(result)


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
