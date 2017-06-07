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

# Import file
from readTextFile import *
# Used Libraries
import re


#--- Testing
testObj = engTextFromTxt3(inputFile3,encodingType)
#w_breaks = testObj.split(unwantedRegexes[0])
print("\n")# \n \n")
#print(w_breaks)

# Add appostrophes
def byteToString( byteString ):
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

def removeEndPunct( inString ):
    " take in string, output string without punctuation at ends of words
    "

#print(testObj)
#print("\n \n \n")
newString = byteToString(testObj)
print(newString)
print("\n")
lNewString = newString.lower()
print(lNewString)
