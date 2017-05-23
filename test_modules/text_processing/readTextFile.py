"""
    Create Function(s) That
    - Read in Files
"""
# Used Libraries
import re

# Constants
inputFile = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\raven.txt"
encodingType = "IBM500"

# Helpers

def engTextFromTxt(inputFile,encodingType):
    """ 
        read text file using western european fonts
    """
    with open(file=inputFile,mode='r', encoding=encodingType) as inputText:
        read_data = inputText.read()
        rText = read_data.encode(encoding=encodingType, errors="strict")
        return(rText)

#Testing
testObj = engTextFromTxt(inputFile,encodingType)

print("\n \n \n")
print(type(testObj))
print("\n \n \n")
print(testObj)
