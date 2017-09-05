import pandas
import pickle

"""
 Match Phonemes to Scale Degree by probabilities

 Alg:
    Pre - processing
    - determine each phoneme's percentage of total phoneme occurences
    - determine each major scale degree's percentage of total occurrences

    Initial Sort
    - sort phoneme percentage holding structure from high to low
    - sort scale degree percentage holding structure from high to low

    Create a structure S where
        - each scale degree is listed
        - each scale degree has it's own unique bucket b, with capacitiy C_b
        - each bucket has a list, Lphone_b, that lists phoenemes assigned to it
            - initial lists = []
        - each bucket has a list, Lam_b, that lists phoneme weights assigned to it
            - inital lists = []
        - each phoneme stored has an amount stored, a_p,b = sum of the elements of Lam_b
            - initial amounts = 0
        - each bucket has a remainder of C_b - a_p,b
            - initial amounts = C_b

    0. Initialize
        - empty scale degree/ phoneme assignment structure
        - empty mapping dictionary
    1. For each phoneme in phonemes percentages holding structure
        i. Sort structure from highest remainder to lowest remainder
        ii. Assign phoneme to Lphoneme_highestRemainder
        iii. Update the phoneme weight's list for bucket highest remainder
        iv. Update the amount stored for the bucket highest remainder
        v. Update remainder for bucket highest remainder
    2. For each scale degree bucket
            For each phoneme in the assigned list
                i. Add a dicionary entry with phoneme: scale-degree
"""
def init_assignment_structure(scaleDegListPickle):
    dictionary = pandas.read_pickle(scaleDegListPickle)
    dictionary = dictionary.drop(dictionary.index[7])
    sumOccurences = dictionary["# of occurences"].sum()
    dictionary["capacity"] = dictionary["# of occurences"]/sumOccurences
    numDegrees = len(dictionary["# of occurences"])
    emptyList = [[]for i in range(0,numDegrees)]
    emptyList2 = [[]for i in range(0,numDegrees)]
    #zeroList = [0 for i in range(0,numDegrees)]
    dictionary["phonemes"] = pandas.Series(emptyList)
    dictionary["phoneme weights"] = pandas.Series(emptyList2)
    #dictionary["current weight"] = pandas.Series(zeroList)
    dictionary["remainder"] = dictionary["capacity"]
    dictionary = dictionary.sort_values(ascending=False,by="remainder")
    return(dictionary)

def assignPhonemesToNotes(scaleDegListPickle,phonemeDF):
    # initialize
    #phonemeMappingDictionary = {} #phoneme output dictionary
    structure = init_assignment_structure(scaleDegListPickle) # phoneme/note mapping structure

    #for index, row in phonemeDF.iterrows():
    phonemeLen = len(phonemeDF["phoneme"])
    for i in range(0,phonemeLen):
        phoneme = phonemeDF.get_value(index=i,col="phoneme")
        percentage = phonemeDF.get_value(index=i,col="percentages")

        # sort structure from high remainder to low
        structure = structure.sort_values(ascending=False, by="remainder")

        # get first index
        first = structure.first_valid_index()

        # Assign phoneme to highest remainder byteToString
        newPList = structure.get_value(index=first,col="phonemes")
        newPList.append(phoneme)
        structure.set_value(index=first,col="phonemes",value=newPList)

        # List phoneme weights
        newPWList = structure.get_value(index=first,col="phoneme weights")
        newPWList.append(percentage)
        structure.set_value( index=first, col="phoneme weights", value=newPWList )

        # Calculate total phoneme weights
        #weight = structure.get_value(index=first,col="current weight")
        #weight = sum(newPWList)
        #structure.set_value(index=first, col="current weight", value = weight)

        capacity = structure.get_value(index=first,col="remainder")
        capacity = capacity - percentage
        structure.set_value(index=first, col="remainder", value = capacity)

    return(structure)
    #return(phonemeMappingDictionary)
