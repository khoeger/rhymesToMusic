"""
The functions here help take output from
FEASEPUMP AB AMPL NEOS SERVER output
and format it as a useable dictionary format.
"""

#def extractDegPhon(inputFile):
#    """
#        Given input file
#        - search
#        - extract degree, extract phoneme
#        - assign
#    """
import re

def listAssignments(readFile):
    """
    Given input read file from FEASEPUMP AB output,
        - analyze file for pattern
        - return list of strings of pattern
    """
    pattern = "amountPlaced\[[\d]+,'[A-Z]+'\]"
    rePattern = re.compile(pattern)
    patternList = rePattern.findall(readFile)
    return(patternList)

def extractDegreePhonemeString(inString, scaleDegreePattern, phonemePattern):
    """
    Given a string, sdPatt, pPatt return wanted degree, phoneme
    """
    #scaleDegreePattern = "\d"
    #phonemePattern =  "'[A-X]+'"
    scaleDeg = int(scaleDegreePattern.findall(inString)[0])
    phonemeStr = phonemePattern.findall(inString)[-1]
    return([phonemeStr, scaleDeg])

def phonemeListToDictEntries(inlist,dictionary,common):
    for entry in inlist:
        dictionary[entry] = common
    return(dictionary)

def createDictionary(structure):
    dictionary = {}
    structureLen = len(structure["scale degree"])
    for i in range(0,structureLen):
        common = int(structure.get_value(index=i,col="scale degree"))
        inlist = structure.get_value(index=i,col="phonemes")
        phonemeListToDictEntries(inlist,dictionary,common)
    return(dictionary)

def degPhonemeDict(inStringList):
    """
    Given a string list:
    - initiate dictionary
    - for each element of list
        - extract scale degree
        - extract phoneme pattern
        - assign dictionary mapping
    - return dicitionary
    """
    phonemeToDegreeDict = {}
    scaleDegreePattern = re.compile("\d")
    phonemePattern =  re.compile("[A-Z]+")

    for element in inStringList:
        [phonemeStr, scaleDeg] = extractDegreePhonemeString(element,scaleDegreePattern,phonemePattern)
        phonemeToDegreeDict[phonemeStr] = scaleDeg
    return phonemeToDegreeDict
