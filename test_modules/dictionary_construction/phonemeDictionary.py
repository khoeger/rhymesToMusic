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


# Testing
#print(cleanPList)
""" Figure out how to import clean list later"""
cleanList = [['AY'], ['HH', 'EY', 'T'], ['DH', 'AH'], ['W', 'EY'], ['Y', 'UW'], ['T', 'AO', 'K'], ['T', 'UW'], ['M', 'IY'], ['AH', 'N', 'D'], ['DH', 'AH'], ['W', 'EY'], ['Y', 'UW'], ['K', 'AH', 'T'], ['Y', 'AO', 'R'], ['HH', 'EH', 'R'], ['AY'], ['HH', 'EY', 'T'], ['DH', 'AH'], ['W', 'EY'], ['Y', 'UW'], ['D', 'R', 'AY', 'V'], ['M', 'AY'], ['K', 'AA', 'R'], ['AY'], ['HH', 'EY', 'T'], ['IH', 'T'], ['W', 'EH', 'N'], ['Y', 'UW'], ['S', 'T', 'EH', 'R'], ['AY'], ['HH', 'EY', 'T'], ['Y', 'AO', 'R'], ['B', 'IH', 'G'], ['D', 'AH', 'M'], ['K', 'AA', 'M', 'B', 'AE', 'T'], ['B', 'UW', 'T', 'S'], ['AH', 'N', 'D'], ['DH', 'AH'], ['W', 'EY'], ['Y', 'UW'], ['R', 'EH', 'D'], ['M', 'AY'], ['M', 'AY', 'N', 'D'], ['AY'], ['HH', 'EY', 'T'], ['Y', 'UW'], ['S', 'OW'], ['M', 'AH', 'CH'], ['DH', 'AE', 'T'], ['IH', 'T'], ['M', 'EY', 'K', 'S'], ['M', 'IY'], ['S', 'IH', 'K'], ['IH', 'T'], ['IY', 'V', 'IH', 'N'], ['M', 'EY', 'K', 'S'], ['M', 'IY'], ['R', 'AY', 'M'], ['AY'], ['HH', 'EY', 'T'], ['DH', 'AH'], ['W', 'EY'], ['Y', 'UH', 'R'], ['AO', 'L', 'W', 'EY', 'Z'], ['R', 'AY', 'T'], ['AY'], ['HH', 'EY', 'T'], ['IH', 'T'], ['W', 'EH', 'N'], ['Y', 'UW'], ['L', 'AY'], ['AY'], ['HH', 'EY', 'T'], ['IH', 'T'], ['W', 'EH', 'N'], ['Y', 'UW'], ['M', 'EY', 'K'], ['M', 'IY'], ['L', 'AE', 'F'], ['IY', 'V', 'IH', 'N'], ['W', 'ER', 'S'], ['W', 'EH', 'N'], ['Y', 'UW'], ['M', 'EY', 'K'], ['M', 'IY'], ['K', 'R', 'AY'], ['AY'], ['HH', 'EY', 'T'], ['DH', 'AH'], ['W', 'EY'], ['Y', 'UH', 'R'], ['N', 'AA', 'T'], ['ER', 'AW', 'N', 'D'], ['AH', 'N', 'D'], ['DH', 'AH'], ['F', 'AE', 'K', 'T'], ['DH', 'AE', 'T'], ['Y', 'UW'], ['D', 'IH', 'D', 'AH', 'N', 'T'], ['K', 'AO', 'L'], ['B', 'AH', 'T'], ['M', 'OW', 'S', 'T', 'L', 'IY'], ['AY'], ['HH', 'EY', 'T'], ['DH', 'AH'], ['W', 'EY'], ['AY'], ['D', 'OW', 'N', 'T'], ['HH', 'EY', 'T'], ['Y', 'UW'], ['N', 'AA', 'T'], ['IY', 'V', 'IH', 'N'], ['K', 'L', 'OW', 'S'], ['N', 'AA', 'T'], ['IY', 'V', 'IH', 'N'], ['AH'], ['L', 'IH', 'T', 'AH', 'L'], ['B', 'IH', 'T'], ['N', 'AA', 'T'], ['IY', 'V', 'IH', 'N'], ['AE', 'T'], ['AO', 'L']]

print(cleanList[30])
out = tallySublist(cleanList[30],{})
print(out)
out2 = tallyList(cleanList,{})
print(out2)
