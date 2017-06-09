"""
    clean file of unwanted Regular Expressions
"""
"""
# Unwanted RegExs
unwantedRegexes =   ["%\\n",
                    "\\xe2\\x80\\x94",
                    "\\xe2\\x80\\x9c",
                    "\\xe2\\x80\\x99",
                    "\\xe2\\x80\\x9d",
                    ]

# Attempt to place unwanted Regexes back into the stream
"""

"""
# Import file
from readTextFile import *
# Used Libraries
"""
import re
#"""

"""
#--- Testing
testObj = engTextFromTxt3(inputFile3,encodingType)
#w_breaks = testObj.split(unwantedRegexes[0])
#print("\n")# \n \n")
#print(w_breaks)
"""

#---
# Helper functions
#---

# Add appostrophes
def byteToString( byteString , encodingType ):
    """ - Still has issues with other input
        - runs using inputFile3 only currently
        - works with 'python -E test_modules\\text_processing\\textCleaning.py PYTHONLEGACYWINDOWSSTDIO'
    """
    pattern = "\\xe2\\x80\\x99"
    repl = "'"
    bytesToString = byteString.decode(encodingType,errors="ignore")
    #print(type(bytesToString))
    #newString = re.sub(pattern, repl, bytesToString)
    return(bytesToString)#newString)

def removeEdgePuncts( inString ):
    """ take in string, output string without punctuation at ends of words
    """
    pattern1 = "[\n ][^a-zA-Z]+"
    pattern2 = "[^a-zA-Z]+[\n ]"
    repl = " "
    noFrontPunc = re.sub(pattern1,repl,inString)
    noEndPunc = re.sub(pattern2,repl, noFrontPunc)
    return(noEndPunc)

def removeNums( string ):
    """ if there is a number in a string, remove the number
    """
    pattern = "[0-9]+"
    repl = ""
    newString = re.sub(pattern,repl,string)
    return(newString)

    ### Wrong package? Called by wordsToPhonemes's clean phoneme list (BELOW)
def rmNumsFrmStrList( stringList ):
    """ replace strings in  stringList with numberless strings """
    for i in range(0,len(stringList)):
        string = stringList[i]
        newString = removeNums(string)
        stringList[i]=newString
    return(stringList)




"""
#print(testObj)
#print("\n \n \n")
newString = byteToString(testObj)
#print(newString)
#print("\n")
lNewString = newString.lower()
#print(lNewString)
#print("\n")
remPunc = removeEdgePuncts(lNewString)
#print(remPunc)
"""
