"""
Run demo melody conversion
"""
print("\n \n ")
print("~Converting text to melody~\n")

print("\n... Loading packages...\n")
import re
import music21 as mus
from nltk.corpus import cmudict
from nltk.tokenize import TweetTokenizer
import pandas
import pickle

print(  "\nWhen inputting text, please do not use punctuation, apart",
        " from typically used contractions. \nPlease do not use slang.",
        " \nPlease use English.\n")

inputText = input("Please enter a string of text to convert: \n\n")

scaleType = input("\nChoose a type of scale: \n    major\n    minor \n\n")

print("\nGenerating a melody in a "+scaleType+" key using your input text.\n")
