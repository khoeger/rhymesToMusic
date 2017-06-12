"""
    Clean pieces
    ------------
    -   Normalize music pieces so that they are in the same starting key
    -
    ------------
    Katarina Hoeger
    June 9, 2017
"""

import music21 as mus

"""
    Helpers
"""
# Transpose Melody
def transposeMelody( melody_line , melody_key, final_major_key , final_minor_key ):
    """
        Input: flattened melody without repeats
        Process: Pass to subTransposeMelody
        Output: Melody in correct major/minor key
    """
    if melody_key.mode == 'major':
        return(subTransposeMelody( melody_line , melody_key.tonic , final_major_key))
    elif  melody_key.mode == 'minor':
        return(subTransposeMelody( melody_line , melody_key.tonic , final_minor_key))
    else:
        print('Failed to tranpose melody.\n')


def subTransposeMelody( melody_line, melody_tonic , final_key ):
    """
        Transpose melody
    """
    current_tonic = mus.note.Note(melody_tonic)
    final_tonic = mus.note.Note(final_key)
    interval_wanted = mus.interval.notesToChromatic( current_tonic , final_tonic )
    transposed_melody = melody_line.flat.transpose(interval_wanted.getDiatonic().directedName)
    return(transposed_melody)
