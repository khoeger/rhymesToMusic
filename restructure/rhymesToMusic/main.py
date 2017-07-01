"""
A place where I can test all of my code together
while I figure out how to build a project in
Python properly - complete with testing suite, etc.

Currently:
    - list all imports
    - list any necessary constants
    - Functions
        - read text -> clean text -> extract phonemes
    - Test
        - read text -> clean text -> extract phonemes

Future:
    - make a proper testing suite, outside of this folder

To Run:
    python -E restructure\rhymesToMusic\main.py PYTHONLEGACYWINDOWSSTDIO

Katarina Hoeger
June 2017
"""

"""
#   Packages
"""
print("Loading Packages ...")
import re # Had to import manually in textCleaning.py.. Why?
import music21 as mus # Had to import into read_corpus.py, cleanPieces.py
from nltk.corpus import cmudict
from nltk.tokenize import TweetTokenizer


"""
#   Helper function module imports
"""
from text_processing.readTextFile import *
from text_processing.textCleaning import *
from text_processing.wordsToPhonemes import *
from dictionary_construction.phonemeDictionary import *
from music_processing.read_corpus import *
from music_processing.cleanPieces import *
from dictionary_construction.noteFreqDictionary import *
from numerical_operations.dictionaryEntries import *
from numerical_operations.createAMPL import *
from numerical_operations.outputToDict import *
from parseTextAsMusic.parseText import *
"""
#   Constants
"""
print("Loading Constants & Inputs ...")
inputFile = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\raven.txt"
inputFile2 = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\handkerchief.txt"
inputFile3 = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\10things.txt"
feasepumpFile = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\restructure\\rhymesToMusic\\numerical_operations\\FeasepumpAB_6_18_2017.txt"
encodingType2 = "utf-8"#"IBM500" #"utf-8"
corpus_chosen = 'airdsAirs'
final_major_key = 'C5'#'F#4'
final_minor_key = 'A4'#'Eb4'
AMPLDatFilepath = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\restructure\\rhymesToMusic\\numerical_operations\\assignPhonemesNotes.dat"
AMPLModFilepath = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\restructure\\rhymesToMusic\\numerical_operations\\assignPhonemesNotes.mod"
AMPLRunFilepath = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\restructure\\rhymesToMusic\\numerical_operations\\assignPhonemesNotes.run"
weight = "1000"
assignments = "1"
outputPath = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_output\\"


"""
    Pre-calculated
"""
d = cmudict.dict()
tknzr = TweetTokenizer()
majScale = mus.scale.MajorScale(final_major_key)
minScale = mus.scale.MinorScale(final_minor_key)
minorDict = {}
majorDict = {}

"""
    Testing

    to run, type
        wordList = tknzr.tokenize(remPunc)
    into cmd.exe in this folder
"""
print("\n \n \n")
print("Test Read")
testRead = engTextFromTxt3(inputFile3,encodingType2)
print(testRead)

print("\n \n \n")
print("New String, lower, w/out ending punctuation")
newString = byteToString(testRead , encodingType2).lower()
remPunc = removeEdgePuncts(newString)
#print(remPunc)

#print("\n \n \n")
print("Word list")
wordList = tknzr.tokenize(remPunc)
#print(wordList)

#print("\n \n \n")
print("Phoneme List, with stress marks")
phonemesOut = wordL2phonemeL(wordList,d)
print(phonemesOut[0])

#print("\n \n \n")
print("Missing words list")
#print(phonemesOut[1])

#print("\n \n \n")
print("Phoneme list, without stress marks")
cleanList = cleanPhonemeList(phonemesOut[0])
#print(cleanList)

#print("\n \n \n")
print("Tally Phonemes in Dictionary\n")
phonemeDictionary = tallyList(cleanList,{})
print(phonemeDictionary)

print("\n \n \n")
print("Accessing Corpus")
corpusElements = listElementsOfCorpus( corpus_chosen )
#print(corpusElements[0])

#print("\n \n \n")
print("Clean individual piece")
samplePiece = corpusElements[0].expandRepeats()
samplePiece = corpusElements[0].flat
sampleKey = samplePiece.analyze('key')
sampleTranspose = transposeMelody(samplePiece, sampleKey, final_major_key, final_minor_key)
#sampleTranspose.show('lily')
#sampleTranspose.show('midi')


"""
    Modularize better!!!!
"""


#print("\n \n \n")
print("Count degree occurrences")
#pitchList = sampleTranspose.pitches
#shortPitchList[0] = [str(p) for p in pitchList]
#majScale = mus.scale.Maj
for pieceNo in range(0,len(corpusElements)):
    melody = corpusElements[pieceNo]#.expandRepeats()
    #melody = melody.flat
    melodyKey = melody.analyze('key')
    melodyTranspose = transposeMelody(melody, melodyKey, final_major_key, final_minor_key)
    pitchList = melodyTranspose.pitches
    shortPitchList = [str(p) for p in pitchList]
    [majorDict, minorDict] = countDegrees(shortPitchList, minorDict, majorDict, melodyKey.mode, majScale, minScale)
print('\n')
print("Major Key Scale Degree Frequency Dictionary")
print(majorDict)
print('\n')
print("Minor Key Scale Degree Frequency Dictionary")
print(minorDict)
print('\n')

print("Tally dictionary size: Phonemes")
tallyPhonemes = sumDictValues(phonemeDictionary)
print(tallyPhonemes)
print('\n')

print("Tally dictionary size: Major Dictionary")
tallyMajDict = sumDictValues(majorDict)
print(tallyMajDict)
print('\n')

print("Tally dictionary size: Minor Dictionary")
tallyMinorDictionary = sumDictValues(minorDict)
print(tallyMinorDictionary)
print('\n')

print("Write .dat file at")
print(AMPLDatFilepath)
constructDatFile(AMPLDatFilepath, majorDict, tallyMajDict, phonemeDictionary, tallyPhonemes, weight, assignments)

"""
    Insert MISSING section on running AMPL NEOS server
"""
#print('\n')
print('\n')
print("Extracting Feaspump AB results")
feasepumpByte = engTextFromTxt3(feasepumpFile,encodingType2)
#print('\n')
print("Feasepump Byte")
#print(feasepumpByte)
#print('\n')
print("Feasepump Read")
feasepumpRead = byteToString(feasepumpByte,encodingType2)
#print('\n')
print("Feasepump Assignment List")
listOfAssignments = listAssignments(feasepumpRead)
#print(listOfAssignments)
print('\n')
print("Build Phoneme, Degree Dictionary")
phonemeDegreeDictionary = degPhonemeDict(listOfAssignments)
print(phonemeDegreeDictionary)

"""
    Translate Text to Music using Dictionary
    - read text file
    - break text into list of words + punctuation
    - beginning & end punctuation
        - *For right now* All [A-Z]' characters are a rest
        - commas , -, -- , ; ,: are a beat rests.
        - periods/exclamation points, question marks are two beats rests
        - quotation marks are ignored
        - new lines means start a new measure, rests fill rest of measure.
        - two new lines means more than 1 measure of rest
    - each word
        - if a word is unknown: FIX LATER - skip
        - for known words:
            - break word into phonemes
            - *For right now* ignore stresses
            - *For right now* words are  measures
            - *For right now* break measures into syllable sections for rhythm
"""
# Read Text file = newString
readPoemText = newString
# Poem to "Chunks"
chunkList = readPoemText.split()
print("\nChunk List")
print(chunkList)

print("\nConvert select words to music")
entireOutputPath1 = outputPath+"measure1.mid"
measure1 = buildMeasure(chunkList[0],d,phonemeDegreeDictionary,majScale)
measure1.write('midi',entireOutputPath1)
measure1.show('lily')
entireOutputPath2 = outputPath+"10things_major.mid"#"measure1.mid"
print("\nBuild  piece, measure by measure")
piece = buildPiece(chunkList,d,phonemeDegreeDictionary,majScale)
print("\nOutput useable piece information")
piece.write('midi',entireOutputPath2)
piece.show("lily")
