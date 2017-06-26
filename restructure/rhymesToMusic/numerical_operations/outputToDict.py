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

def extractDegreePhonemeString(inString, sdPatt, pPatt):
    """
    Given a string, sdPatt, pPatt return wanted degree, phoneme
    """
    #scaleDegreePattern = "\d"
    #phonemePattern =  "'[A-X]+'"
    scaleDeg = int(sdPatt.findall(inString))
    phonemePatt = pPatt.findall(inString)
    return([phonemePatt, scaleDeg])
