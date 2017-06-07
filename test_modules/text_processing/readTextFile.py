"""
    Create Function(s) That
    - Read in Files
"""

# Constants
inputFile = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\raven.txt"
inputFile2 = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\handkerchief.txt"
inputFile3 = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\10things.txt"
encodingType = "utf-8"#"IBM500" #"utf-8"
unwantedRegexes =   ["%\\n",
                    "\\xe2\\x80\\x94",
                    "\\xe2\\x80\\x9c",
                    "\\xe2\\x80\\x99",
                    "\\xe2\\x80\\x9d"
                    ]

#set PYTHONIOENCODING = utf-8

# Helpers
"""def engTextFromTxt(inputFile,encodingType):
    #
    #    read text file using western european fonts
    #
    with open(file=inputFile,mode='r', encoding=encodingType) as inputText:
        read_data = inputText.read()
        rText = read_data.encode(encoding=encodingType, errors="strict")
        print("mode 'r'")
        print("read_data")
        print(type(read_data))
        print(len(read_data))
        inputText.close()
    return(rText)
        #return(read_data)
"""
def engTextFromTxt2(inputFile,encodingType,unwantedRegexes):
    #"
    #    split file into new lines
    #    read text file
    #"
    with open(file=inputFile,mode='r', encoding=encodingType) as inputText:
        read_data = inputText.read()
        #rText = read_data.encode(encoding=encodingType, errors="strict")
        rBreaks = read_data.split(unwantedRegexes[0])
        print(len(rBreaks))
        for i in rBreaks:
            rText = type(i)#i.encode(encoding=encodingType, errors="strict")
            print(rText)
        #return(rText)

def engTextFromTxt3(inputFile,encodingType):
    #"
        #read text file using western european fonts
    #"
    with open(file=inputFile,mode='r+t', encoding=encodingType) as inputText:
        read_data = inputText.read()
        #print(type(read_data))
        #print(len(read_data))
        rText = read_data.encode(encoding=encodingType, errors="strict")
        #print(type(rText))
    return(rText)
        #return(read_data)

def engTextFromTxt4(inputFile,encodingType):
    #""" DOESN"T WORK
    #    read text file using western european fonts
    #"""
    with open(file=inputFile,mode='r', encoding=encodingType) as inputText:
        read_data = inputText.read()
        inputText.close()
    return(read_data)
        #return(read_data)

def engTextFromTxt5(inputFile,encodingType):
    #"
        #read text file using western european fonts
    #"
    with open(file=inputFile,mode='r+t', encoding=encodingType) as inputText:
        sText = inputText.read()
        print(type(sText))
        print(len(sText))
        bText = sText.encode(encoding=encodingType, errors="backslashreplace") #errors="strict"
        print(type(bText))
        strText = bText.decode(encoding=encodingType, errors="backslashreplace")
        print(type(strText))
    #return(rText)
    return(strText)
"""
#Testing
#testObj = engTextFromTxt(inputFile,encodingType)
#testObj2 = engTextFromTxt2(inputFile,encodingType,unwantedRegexes)
#testObj3 = engTextFromTxt3(inputFile,encodingType)
testObj4 = engTextFromTxt3(inputFile3,encodingType)
print("\n \n \n")
#print(type(testObj4))
print("\n \n \n")
print(testObj4)
"""
