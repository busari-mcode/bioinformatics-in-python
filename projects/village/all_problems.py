# ********* Strings and Lists ************
wordOneStartPos = 22
wordOneEndPos = 27

wordTwoStartPos = 97
wordTwoEndPos = 102

txtStr = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"

        # Note: end position is not inclusive, so we add 1 to capture it
print(
    f'{txtStr[wordOneStartPos:wordOneEndPos + 1]} {txtStr[wordTwoStartPos:wordTwoEndPos + 1]}'
)
