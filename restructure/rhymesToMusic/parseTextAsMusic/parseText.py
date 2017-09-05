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
from nltk.corpus import cmudict
import re
import music21 as mus
from text_processing.wordsToPhonemes import *

d = cmudict.dict()

#-------------------------------
def isPunctuation(chunk):
    pattern = re.compile("[^a-zA-Z]+")
    punctuationList = re.findall(pattern,chunk)
    return(punctuationList)

def letterOrNot(chunkPiece,pattern):
    if re.findall(pattern,chunkPiece)==[]:
        return("letter")
    else:
        return("other")

def punctuationSlots(chunk,punctuationList):
    pattern = re.compile("[^a-zA-Z]+")

    front = chunk[0]
    end = chunk[-1]

    # is the first char a letter?
    firstChar = letterOrNot(front,pattern)
    if firstChar == "letter":
        pass
    return("ADD A VALUE")

def frontPunctuation(chunk):
    pattern = re.compile("[\n ][^a-zA-Z0-9]+")
    frontPunc = re.findall(pattern,chunk)
    if frontPunc == []:
        return("")
    else:
        return(frontPunc[0])

def endPunctuation(chunk):
    pattern = re.compile("[^a-zA-Z0-9]+[\n ]")
    endPunc = re.findall(pattern,chunk)
    if endPunc == []:
        return("")
    else:
        return(endPunc[0])

def textChunk(chunk):
    pattern1 = re.compile("[\n ][^a-zA-Z0-9]+")
    pattern2 = re.compile("[^a-zA-Z0-9]+[\n ]")
    chunk0 = re.sub(pattern1, "", chunk)
    chunk1 = re.sub(pattern2, "", chunk0)
    return(chunk1)

def phonemeToPitchVal(dictionary,phoneme,scale):
    #print("Phoneme","type(phoneme)")
    #print(phoneme,type(phoneme))
    if phoneme in dictionary.keys():
        noteDegree = dictionary[phoneme]
        freq = scale.pitchFromDegree(noteDegree)
        return(freq)
    else:
        return("[parseText.py: phonemeToPitchVal] ",
            "Error converting degree to frequency. ",
            "Phoneme not in the dictionary")


def buildMeasure(chunk,d,dictionary,scale):
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
    tChunk = tChunk.lower()
    ePuncChunk = endPunctuation(chunk)

    print("Front punctuation")
    print(fPuncChunk)
    print("Word Chunk")
    print(tChunk)
    print("End Chunk")
    print(ePuncChunk)

    measure = mus.stream.Stream()
    convertList = []

    if fPuncChunk != '':
        convertList.append('REST')
    if textChunk != '':
        #textChunkOn = 1
        textChunkPhonemes = word2Phoneme(chunk,d)
        textChunkPhonemesClean = rmNumsFrmStrList(textChunkPhonemes)
        #textChunkPhonemeLen = len(textChunkPhonemesClean)
        convertList = convertList + textChunkPhonemesClean
    if ePuncChunk != '':
        convertList.append('REST')
    #print("convertList")
    #print(convertList)
    mParts = len(convertList)
    #print("mParts")
    #print(mParts)
    noteLength = 4/mParts
    #print("noteLength")
    #print(noteLength)

    dur = mus.duration.Duration(noteLength)

    for element in convertList:
        print("element is")
        print(element)
        if element == 'REST':
            charRest = mus.note.Rest()
            charRest.duration = dur
            measure.append(charRest)
        else:
            pVal = phonemeToPitchVal(dictionary,element,scale)
            print("pval,type(pval)")
            print(pVal,type(pVal))
            pValNote = mus.note.Note(pVal)
            pValNote.duration = dur
            measure.append(pValNote)

    return(measure)

def buildPiece(chunkList,d,dictionary,scale):
    piece = mus.stream.Stream()
    #for chunk in chunkList:
    for i in range(0,len(chunkList)):
        print(i)
        print(chunkList[i])
        #measure = buildMeasure(chunk,d,dictionary,scale)
        measure = buildMeasure(chunkList[i],d,dictionary,scale)
        print("measure created!")
        piece.append(measure)
    return(piece)
