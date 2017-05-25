"""
    Create Function(s) That
    - Read in Files
"""
# Constants
inputFile = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\raven.txt"
encodingType = "IBM500"
unwantedRegexes =   ["%\\n",
                    "\\xe2\\x80\\x94",
                    "\\xe2\\x80\\x9c",
                    "\\xe2\\x80\\x99",
                    "\\xe2\\x80\\x9d"
                    ]

# Helpers
def engTextFromTxt(inputFile,encodingType):
    """
        read text file using western european fonts
    """
    with open(file=inputFile,mode='r', encoding=encodingType) as inputText:
        read_data = inputText.read()
        rText = read_data.encode(encoding=encodingType, errors="strict")
        return(rText)

def engTextFromTxt2(inputFile,encodingType,unwantedRegexes):
    """
        split file into new lines
        read text file
    """
    with open(file=inputFile,mode='r', encoding=encodingType) as inputText:
        read_data = inputText.read()
        #rText = read_data.encode(encoding=encodingType, errors="strict")
        rBreaks = read_data.split(unwantedRegexes[0])
        print(len(rBreaks))
        for i in rBreaks:
            rText = type(i)#i.encode(encoding=encodingType, errors="strict")
            print(rText)
        #return(rText)

#Testing
testObj = engTextFromTxt(inputFile,encodingType)
testObj2 = engTextFromTxt2(inputFile,encodingType,unwantedRegexes)

print("\n \n \n")
print(type(testObj))
print("\n \n \n")
print(testObj)
