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

#def phraseMaker(inString):
#    """
#    A phrase is a line w/out newline? Or with period.
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
