"""
    Need to convert music to text in some way
        Goal
            - read characters in string by "type"
            - if a character is type [], then follow rules to write melody
            - output melody

    For purposes of having a working conversion
        - read characters in string by "type"
        - types: words =[a-zA-Z]+ and [[a-zA-Z]+'[a-zA-Z]+], non words else
"""
import nltk.corpus import cmudict
import re
import music21 as mus
from rhymesToMusic.text_processing.wordsToPhonemes import *

d = cmudict.dict()

#-------------------------------

#def phraseMaker(inString):
#    """
#    A phrase is a line w/out newline? Or with period.
#    Break input section into phrases (Also need function to break into sections)
#    """

def buildMeasure(chunk):
    """
        Given an input chunk:
        - Separate chunk into frontPunctuation, text, endPunctuation
            - break text chunk into syllable chunks
            - create a chunk piece list composed of all composite chunks
        - determine measure rhythm from chunk list length
        - build measure
    """
    fPuncChunk = frontPunctuation(chunk)
    tChunk = textChunk(chunk)
    ePuncChunk = endPunctuation(chunk)

    measure = mus.stream.Stream()
    fPuncChunkOn = 0
    texChunkOn = 0
    ePuncChunkOn = 0
    convertList = []

    if fPuncChunk != '':
        fPuncChunkOn = 1
        convertList.append('REST')
    if textChunk != '':
        #textChunkOn = 1
        textChunkPhonemes = word2Phoneme(chunk,d)
        textChunkPhonemesClean = cleanPhonemeList(textChunkPhonemes)
        #textChunkPhonemeLen = len(textChunkPhonemesClean)
        convertList = convertList + textChunkPhonemesClean
    if ePuncChunk != '':
        ePuncChunkOn = 1
        convertList.append('REST')

    mParts = len(convertList)
    noteLenth = 4/mParts

    dur = mus.duration.Duration(noteLength)

    for element in convertList:
        if element == 'REST':
            charRest = mus.note.Rest()
            charRest.duration = dur
            measure.append(charRest)
        else:
            pVal = phonemeToPitchVal(dictionary,phoneme)
            pValNote = mus.note.Note(pVal)
            pValNote.duration = dur
            measure.append(pValNote)
