"""
Run demo melody conversion
"""
print("\n \n ")
print("~Converting text to melody~\n")
print(  "\nWhen inputting text, please do not use punctuation, apart",
        " from typically used contractions. \nPlease do not use slang.",
        " \nPlease use English.\n")

inputText = input("Please enter a string of text to convert: \n\n")

scaleType = input("\nChoose a type of scale: \n    major\n    minor \n\n")

print("\nGenerating a melody in a "+scaleType+" key using your input text.\n")
