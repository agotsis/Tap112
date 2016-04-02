from __future__ import division,print_function
import noteDictionary
import BasicFFT

#create a function that takes a list of frequencies and returns a list of notes
#assumes findNote(freq) converts a float freq to a string note

def freqToNoteList(freqList):
    #freqList is a 2D list of frequencies
    result = []
    for freqs in freqList:
        subResult = []
        for freq in freqs:
            note = findNote(freq)
            subResult.append(note)
        result.append(subResult)
    return result

freqList = maxFFT("420+700Hz.wav")
print(freqToNoteList(freqList))
