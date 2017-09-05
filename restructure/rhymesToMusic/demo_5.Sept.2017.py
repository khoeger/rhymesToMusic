"""
Run demo melody conversion
"""
print("\n \n ")
print("~Converting text to melody~\n")

print("\n... Loading packages & modules ...\n")
import re
import music21 as mus
from nltk.corpus import cmudict
from nltk.tokenize import TweetTokenizer
import pandas
import pickle

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
from dictionary_construction.dictToPandas import *

print("\n... Setting constants ...\n")

encodingType2 = "utf-8"#"IBM500" #"utf-8"
corpus_chosen = 'airdsAirs'
final_major_key = 'C5'#'F#4'
final_minor_key = 'A4'#'Eb4'
outpath = ( "C:\\Users\\katar\\Documents\\2017\\music\\computerMusic",
            "\\CsoundMeetup\\demo_9_5_2017")

# --- User solicitedinput
print(  "\nWhen inputting text, please do not use punctuation, apart",
        " from typically used contractions. \nPlease do not use slang.",
        " \nPlease use English.\n")

inputText = input("Please enter a string of text to convert: \n\n")

scaleType = input("\nChoose a type of scale: \n    major\n    minor \n\n")

outputName = input("\nType an output file name. For example 'filename' will become filename.mid\n\n")
print("\nGenerating a melody in a "+scaleType+" key using your input text.\n")

# --- Pre calculated values
d = cmudict.dict()
tknzr = TweetTokenizer()
majScale = mus.scale.MajorScale(final_major_key)
minScale = mus.scale.MinorScale(final_minor_key)
minorDict = {}
majorDict = {}
print(" ... ")

# --- Start converting the inputText to music
lowerInput = inputText.lower()
wordList = tknzr.tokenize(lowerInput)
phonemesOut = wordL2phonemeL(wordList,d)
cleanList = cleanPhonemeList(phonemesOut[0])
phonemeDictionary = tallyList(cleanList,{})
print(" ... ")
# Corups cleaning things skipped

phonemeSeries = pandas.DataFrame(list(phonemeDictionary.items()),columns=["phoneme","# of occurences"])
phonemeSeriesSum = phonemeSeries["# of occurences"].sum()
phonemeSeries["percentages"] = phonemeSeries["# of occurences"]/phonemeSeriesSum
phonemeSeries = phonemeSeries.sort_values(ascending=False,by="percentages")

pDName = corpus_chosen+"_pdseries_"+scaleType+".pickle"
structure = init_assignment_structure(pDName)
sortedStructure = assignPhonemesToNotes(pDName,phonemeSeries)
phonemeDict = createDictionary(sortedStructure)
print(" ... ")
