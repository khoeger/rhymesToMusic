"""
    - Access corpus chosen
    - Return list of pieces in corpus

    Katarina Hoeger
    June 9, 2017
"""

import music21 as mus

# Helper
def listElementsOfCorpus(corpus_chosen):
    element_list = []
    corpus_accessed = mus.corpus.getComposer(corpus_chosen)
    length_corpus_list = len(corpus_accessed)
    i = 0
    while i < length_corpus_list:
        list_of_pieces = mus.corpus.parse(corpus_accessed[i])
        j = len(list_of_pieces)
        for k in range(0,j):
            element_list.append(list_of_pieces[k])
        i+=1
    return(element_list)
