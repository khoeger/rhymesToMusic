"""
    clean file of unwanted Regular Expressions
"""
"""
# Unwanted RegExs
unwantedRegexes =   ["%\\n",
                    "\\xe2\\x80\\x94",
                    "\\xe2\\x80\\x9c",
                    "\\xe2\\x80\\x99",
                    "\\xe2\\x80\\x9d"
                    ]

# Attempt to place unwanted Regexes back into the stream


# Import file
from readTextFile import *
# Used Libraries
import re


#--- Testing
testObj = engTextFromTxt(inputFile,encodingType)
w_breaks = testObj.split(unwantedRegexes[0])
print("\n \n \n")
print(w_breaks) """
