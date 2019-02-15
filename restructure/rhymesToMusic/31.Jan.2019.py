"""
Run demo melody conversion
- add token parsing of punctuation
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
import sys
import datetime

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
outpath = ( "C:\\Users\\katar\\Documents\\2019\\music\\computerMusic\\projects\\outputs\\rhymesToMusic\\")
nameBeginning = "commonplaces_RK"
inFileName = "restructure\\rhymesToMusic\\poetry\\commonplaces_rudyardKipling.txt"

# --- User solicitedinput
print(  "\nWhen inputting text, please do not use punctuation, apart",
        " from typically used contractions. \nPlease do not use slang.",
        " \nPlease use English.\n")

#inputText = "This is my sample string. \n\n\nWatch out! \n'Tis- snow season."#input("Please enter a string of text to convert: \n\n")
with open( inFileName , encoding='utf8' ) as f:
    read_data =f.read()
#print(read_data)
inputText = read_data
print(type(read_data))
scaleType = "minor"#input("\nChoose a type of scale: \n    major\n    minor \n\n")

outputName = nameBeginning+scaleType+'{:%Y%m%d%H%M}'.format(datetime.datetime.now())#input("\nType an output file name. For example 'filename' will become filename.mid\n\n")
print("\nGenerating a melody in a "+scaleType+" key using your input text.\n")

# --- Pre calculated values
d = cmudict.dict()
tknzr = TweetTokenizer()
if scaleType == 'major':
    usedScale = mus.scale.MajorScale(final_major_key)
elif scaleType == 'minor':
    usedScale = mus.scale.MinorScale(final_minor_key)
else:
    print("The scale given, "+scaleType+", is not a recognized scale. Terminating.")
    sys.exit()
minorDict = {}
majorDict = {}
print(" ... ")

# --- Start converting the inputText to music
lowerInput = inputText.lower()
#print(lowerInput)
# wordList = tknzr.tokenize(lowerInput)
# print(wordList)
doublelinebreaks = re.compile(r"(\n\n)")
stanzas = doublelinebreaks.split(lowerInput)

output_list = []
for stanza in stanzas:
    if stanza == "\n\n":
        #print( "Add measure rest here")
        output_list.append("MeasureRest")

    else:
        #break  extra \n
        newline = re.compile("([\n]+)")
        stanza2 = newline.split(stanza)
        try:
            stanza2.remove('')
        except:
            pass
        # output a list to translate into music
        for i in stanza2:
            output_list.append(i)
#print(output_list)

# break each stanza up by spaces. lose separation
whitespace = re.compile("[ ]+")
output_no_spaces = []
for i in output_list:
    measure = []
    splitWords = whitespace.split(i)
    try:
        splitWords.remove("")
    except:
        pass
    for j in splitWords:
        output_no_spaces.append(j)
#print(output_no_spaces)

# break each measure into punctuation and not
output_measure_input = []
splitText = re.compile(r"(\W+)")
for i in output_no_spaces:
    measure = splitText.split(i)
    try:
        measure.remove('')
        try:
            measure.remove('')
        except:
            pass
    except:
        pass
    output_measure_input.append(measure)
# print(output_measure_input,"\n")

# Translate words into lists of phonemes
phoneme_punctuation_list = []
pure_phonemes = []
#missing_words = []
for measure in output_measure_input:
    to_append = []
    for part in measure:
        #print(part)
        if splitText.fullmatch(part):
            #print("punctuation")
            to_append.append(part)
        elif part == "MeasureRest":
            to_append.append(part)
        else:
            out = wordL2phonemeL([part], d)
            #print(out[0], out[1])
            try:
                for j in out[0][0]:
                    to_append.append(j)
                    pure_phonemes.append(j)
            except:
                pass
            #missing_words.append(out[1])
        #print(to_append)
    phoneme_punctuation_list.append(to_append)

# if sum(missing_words[:][0]) != 0:
#     print("Missing Words Include:",missing_words)

#-- Phoneme to Music Mapping prep
cleanList = cleanPhonemeList(pure_phonemes)

# phonemesOut = wordL2phonemeL(wordList,d)
# print(phonemesOut)
# cleanList = cleanPhonemeList(phonemesOut[0])
phonemeDictionary = tallyList(cleanList,{})
print(" ... ")
# # Corups cleaning things skipped
#
phonemeSeries = pandas.DataFrame(list(phonemeDictionary.items()),columns=["phoneme","# of occurences"])
phonemeSeriesSum = phonemeSeries["# of occurences"].sum()
phonemeSeries["percentages"] = phonemeSeries["# of occurences"]/phonemeSeriesSum
phonemeSeries = phonemeSeries.sort_values(ascending=False,by="percentages")

pDName = corpus_chosen+"_pdseries_"+scaleType+".pickle"
structure = init_assignment_structure(pDName)
sortedStructure = assignPhonemesToNotes(pDName,phonemeSeries)
phonemeDict = createDictionary(sortedStructure)
print(" ... ")
#print(phonemeDict)
#
readText = lowerInput
chunkList2 = readText.split()

chunkList = phoneme_punctuation_list
#print(chunkList)#, "\n", chunkList2,"\n")

musicOutpath = outpath + outputName +".mid"
scoreOutpath = outpath + outputName +".ly"

melodyOut = buildPiece(chunkList,d,phonemeDict,usedScale)
melodyOut.write('midi',musicOutpath)
#melodyOut.write('lily',scoreOutpath)
#melodyOut.show('lily')
melodyOut.show('midi')
