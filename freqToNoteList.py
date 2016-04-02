from __future__ import division,print_function
from noteDictionary import *
from scipy.io.wavfile import read
from BasicFFT import *

#create a function that takes a list of frequencies and returns a list of notes
#assumes findNote(freq) converts a float freq to a string note

def freqToNoteList(freqList):
    #freqList is a 2D list of frequencies
    result = []
    for freqs in freqList:
        subResult = []
        lastNone = False
        for freq in freqs:
            note = findNote(freq)
            if note == None and not lastNone:
                subResult.append(note)
                lastNone=True
            elif note != None:
                subResult.append(note)
                lastNone = False
        result.append(subResult)
    return result

rate, data = read("bin/SMBcut.wav")

freqList = intervalFFT(rate,data,125)
print(freqToNoteList(freqList))
