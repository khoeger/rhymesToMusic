"""
    Count notes in pieces
    Compile frequency of notes in dictionary
"""
import music21 as mus

def countDegrees( pitch_list , minor_dict, major_dict, mode, maj_scale , min_scale):
    """
        * Input: Flattened pitch list, dictionaries, mode, scales
        * Output: countDegreeOccurrence for mode

    """
    if mode == 'major':
        major_dict = countDegOccurrence( pitch_list , major_dict , maj_scale)
    elif mode == "minor":
        minor_dict = countDegOccurrence(  pitch_list , minor_dict, min_scale)
    else:
        print('Neither major or minor key. Error counting degrees.')
    return([major_dict, minor_dict])

def countDegOccurrence( pitch_list, dictionary , final_scale):
    """
        Input: flattened melody line, specific dictionary, final scale
        Output: count the occurences of scale degrees scanned
    """
    for p in pitch_list:
        degP = final_scale.getScaleDegreeFromPitch(p)
        if degP in dictionary.keys():
            dictionary[degP] += 1
        else:
            dictionary[degP] = 1
    return(dictionary)
