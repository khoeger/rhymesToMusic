"""
    Take cleaned word string
    - break into words
    - look up words in cmudict
    - return list of phonemes

    python -E test_modules\text_processing\wordsToPhonemes.py PYTHONLEGACYWINDOWSSTDIO
"""

"""
"""
from text_processing.textCleaning import *
"""
from nltk.corpus import cmudict
from nltk.tokenize import TweetTokenizer

# Constants
d = cmudict.dict()
tknzr = TweetTokenizer()
"""

# Helpers
def word2Phoneme(word,d):
    """
        - take word as input
        - look up phonemes in dict
        - if word has 1 phoneme, return that
        - if word has multiple phonemes, currently choose opt. 1
        - if word has no phonemes, return word as string
    """
    keylist = list(d.keys())
    if word in keylist:
        phonemeOpt = d[word]
        return(phonemeOpt[0])
        #print("Phoneme Options",phonemeOpt)
    else:
        return(word)


def wordL2phonemeL(wordList,d):
    """     - look up each word in wordList
            - if there, add to phonemeList
            - if not there, add to missingWords list

            PROBLEM - Can't clean only one list...
    """
    phonemeList = []
    missingWords = []
    #cleanPhonemeList = []

    numWords = len(wordList)

    for i in range(0,numWords):
        lookup = word2Phoneme(wordList[i],d)
        if isinstance(lookup,str):
            missingWords.append(lookup)
        else:
            phonemeList.append(lookup)
            #lookup2 = lookup
            #cleanLookup = rmNumsFrmStrList(lookup2)
            #cleanPhonemeList.append(cleanLookup)
    #return([phonemeList,cleanPhonemeList,missingWords])
    return([phonemeList,missingWords])

def cleanPhonemeList(phonemeList):
    cleanPList = []
    for i in range(0,len(phonemeList)):
        cleanEntry = rmNumsFrmStrList([phonemeList[i]])
        cleanPList.append(cleanEntry)
    return(cleanPList)
