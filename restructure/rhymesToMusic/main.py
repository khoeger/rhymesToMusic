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

Katarina Hoeger
June 2017
"""

"""
#   Packages
"""
import re # Had to import manually in textCleaning.py.. Why?
import music21 as mus # Had to import into read_corpus.py
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

"""
#   Constants
"""
inputFile = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\raven.txt"
inputFile2 = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\handkerchief.txt"
inputFile3 = "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\10things.txt"
encodingType2 = "utf-8"#"IBM500" #"utf-8"
corpus_chosen = 'airdsAirs'
final_major_key = 'C5'#'F#4'
final_minor_key = 'A4'#'Eb4'


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
#print("\n \n \n")
print("Test Read \n")
testRead = engTextFromTxt3(inputFile3,encodingType2)
print(testRead)

print("\n \n \n")
print("New String, lower, w/out ending punctuation \n")
newString = byteToString(testRead , encodingType2).lower()
remPunc = removeEdgePuncts(newString)
#print(remPunc)

#print("\n \n \n")
print("Word list \n")
wordList = tknzr.tokenize(remPunc)
#print(wordList)

#print("\n \n \n")
print("Phoneme List, with stress marks \n")
phonemesOut = wordL2phonemeL(wordList,d)
#print(phonemesOut[0])

#print("\n \n \n")
print("Missing words list\n")
#print(phonemesOut[1])

#print("\n \n \n")
print("Phoneme list, without stress marks\n")
cleanPList = cleanPhonemeList(phonemesOut[0])
#print(cleanPList)

print("\n \n \n")
print("Tally Phonemes in Dictionary\n")
phonemeDictionary = tallyList(cleanList,{})
print(phonemeDictionary)

print("\n \n \n")
print("Accessing Corpus\n")
corpusElements = listElementsOfCorpus( corpus_chosen )
print(corpusElements[0])
