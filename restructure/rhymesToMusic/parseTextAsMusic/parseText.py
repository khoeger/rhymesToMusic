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
    pattern = re.compile("[\n ]*[^a-zA-Z0-9]+")
    frontPunc = re.findall(pattern,chunk)
    if frontPunc == []:
        return("")
    else:
        return(frontPunc[0])

def endPunctuation(chunk):
    pattern = re.compile("[^a-zA-Z0-9]+[\n ]*")
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

        if element == 'REST':
            charRest = mus.note.Rest()
            charRest.duration = dur
            measure.append(charRest)
        else:
            pVal = phonemeToPitchVal(dictionary,element,scale)
            pValNote = mus.note.Note(pVal)
            pValNote.duration = dur
            measure.append(pValNote)

    return(measure)

def buildMeasure2(chunk,d,dictionary,scale):
    """
        Given an input chunk:
        - determine measure rhythm from chunk list length
        - build measure
    """
    # fPuncChunk = frontPunctuation(chunk)
    # tChunk = textChunk(chunk)
    # tChunk = tChunk.lower()
    # ePuncChunk = endPunctuation(chunk)

    measure = mus.stream.Stream()

    convertList = chunk#[]

    # if fPuncChunk != '':
    #     convertList.append('REST')
    # if textChunk != '':
    #     #textChunkOn = 1
    #     textChunkPhonemes = word2Phoneme(chunk,d)
    #     textChunkPhonemesClean = rmNumsFrmStrList(textChunkPhonemes)
    #     #textChunkPhonemeLen = len(textChunkPhonemesClean)
    #     convertList = convertList + textChunkPhonemesClean
    # if ePuncChunk != '':
    #     convertList.append('REST')
    # #print("convertList")
    # #print(convertList)
    mParts = len(convertList)
    #print("mParts")
    #print(mParts)
    quarters = 4 # quarter notes per measure
    noteLength = quarters/mParts
    #print("noteLength")
    #print(noteLength)

    dur = mus.duration.Duration(noteLength)
    #print(dur)
    punctuation = re.compile(r"(\W+)")

    for element in convertList:

        if element == 'MeasureRest':
            charRest = mus.note.Rest()
            charRest.duration = mus.duration.Duration(quarters/2)
            measure.append(charRest)
        elif punctuation.fullmatch(element):
            charRest = mus.note.Rest()
            charRest.duration = dur#mus.duration.Duration(quarters/(mParts*2)) #dur
            measure.append(charRest)
        else:

            #print(element)
            #print(removeNums(element))
            pVal = phonemeToPitchVal(dictionary,removeNums(element),scale)
            pValNote = mus.note.Note(pVal)
            pValNote.duration = dur
            measure.append(pValNote)

    return(measure)

def buildPiece(chunkList,d,dictionary,scale):
    piece = mus.stream.Stream()
    instr = mus.instrument.Ocarina()
    piece.insert(0.0, instr)
    #for chunk in chunkList:
    for i in range(0,len(chunkList)):
        if chunkList[i] == []:
            pass
        #measure = buildMeasure(chunk,d,dictionary,scale)
        else:
            measure = buildMeasure2(chunkList[i],d,dictionary,scale)
            piece.append(measure)
    return(piece)
"""
--- Learning RE library tricks ---

>>> inputText = "This is my sample string. Long live the Queen!!!! Haha <3 \nSee, it's a new line!"
>>>
>>> pat4 = re.compile(r"([\n]+)")
>>> pat4.split(inputText)
['This is my sample string. Long live the Queen!!!! Haha <3 ', '\n', "See, it's a new line!"]
>>>
>>> pats4 = pat4.split(inputText)
>>> pats4
['This is my sample string. Long live the Queen!!!! Haha <3 ', '\n', "See, it's a new line!"]
>>>
>>> pat3 = re.compile("[ ]+")
>>> pats3 = []
>>> for i in pats4:
...     x = pat3.split(i)
...     for j in x:
...             pats3.append(j)
...
>>> pats3
['This', 'is', 'my', 'sample', 'string.', 'Long', 'live', 'the', 'Queen!!!!', 'Haha', '<3', '', '\n', 'See,', "it's", 'a', 'new', 'line!']
>>>
--- DON'T DO RIGHT AWAY ---
    - also, remove the  ''
>>>
>>> pat2 = re.compile(r"(\W+)"
... )
>>> pats2 = []
>>> for i in pats3:
...     x = pat2.split(i)
...     for j in x:
...             pats2.append(j)
...
>>> pats2
['This', 'is', 'my', 'sample', 'string', '.', '', 'Long', 'live', 'the', 'Queen', '!!!!', '', 'Haha', '', '<', '3', '', '', '\n', '', 'See', ',', '', 'it', "'", 's', 'a', 'new', 'line', '!', '']

"""
