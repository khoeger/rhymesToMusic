"""
Write the functions necessary for creating a phoneme dictionary
- GENERALIZE IN FUTURE TO ALL DICTIONARIES
"""
# Imports
# from test_modules.text_processing.wordsToPhonemes import *
# Constants

# Variables

# Helper functions

def tallySublist( sublist , dictionary ):
    for element in sublist:
        if element in dictionary.keys():
            dictionary[element]+= 1
        else:
            dictionary[element] = 1
    return( dictionary )

def tallyList(inputList, dictionary):
    for sublist in inputList:
        dictionary = tallySublist(sublist, dictionary)
    return(dictionary)
