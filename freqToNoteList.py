from __future__ import division,print_function
from noteDictionary import *
#from scipy.io.wavfile import read
from BasicFFT import *

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

#rate, data = read("SMBcut.wav")

#freqList = intervalFFT(rate,data,250)
#print(freqToNoteList(freqList))