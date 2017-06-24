"""
    Create an AMPL .dat. files using dictionary outputs using
    inputs from dictionaries
"""

def listDictValues(dictionary,tally):
    """
        Create a list of [key, percentage] pairs
    """
    listDictVals = []
    for key in dictionary.keys():
        if key != None:
            percentage = float(dictionary[key])/float(tally)
            listDictVals.append([str(key), str(percentage)])
    return(listDictVals)

def constructDatFile(AMPLDatFilepath, scaleDegreeDictionary, sDTally, phonemeDictionary, pDTally, weight, assignments):#, overwrite = True ):
    """
        - Take in AMPL Filepath
        - Open file @ AMPL Filepath
        - Write following in AMPL format in the .dat file
            - Create a set ScaleDegrees composed of keys of scaleDegreeDictionary, excluding key == None
            - Create a set Phonemes composed of keys of phonemeDictionary
            - Create param phonemeProportions using phonemeDictionary[key]/pDTally
            - Create param scaleDegProportions using scaleDegreeDictionary[key]/sDTally
            - Create param heavyWeight
            - Create param assignmentsAllowed
        - Close file
    """
    #if overwrite == True:
    with open(AMPLDatFilepath,'w') as datFile:
        datFile.write('set ScaleDegrees:= ')
        scaleDegrees = listDictValues(scaleDegreeDictionary,sDTally)
        for degree in scaleDegrees:
            datFile.write(degree[0])
            datFile.write(' ')
        datFile.write(';\n')

        datFile.write('set Phonemes:= ')
        phonemeList = listDictValues(phonemeDictionary,pDTally)
        for phoneme in phonemeList:
            datFile.write(phoneme[0])
            datFile.write(' ')
        datFile.write(';\n\n')

        datFile.write('param: scaleDegProportions :=')
        for degree in scaleDegrees:
            datFile.write('\n'+degree[0]+' '+degree[1])
        datFile.write(' ;\n\n')

        datFile.write('param: phonemeProportions :=')
        for phoneme in phonemeList:
            datFile.write('\n'+phoneme[0]+' '+phoneme[1])
        datFile.write(' ;\n\n')

        datFile.write('param heavyWeight := '+weight+' ; \n')
        datFile.write('param assignmentsAllowed := '+assignments+' ; \n')

    #def constructModFile(AMPLModFilepath, scaleDegreeDictionary, sDTally, phonemeDictionary, pDTally, weight, assignments):
