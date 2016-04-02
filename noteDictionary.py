from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from visual import *

def noteDict():
    nDict = dict()
    #key is the key you press, comment represents note
    nDict['c']=[16.35,17.32,65.41,69.30,32.70,34.65,130.81,
                138.59]#C to Csharp evens
    nDict['d']=[18.35,19.45,36.71,38.89,73.42,77.78,
                146.83,155.56,293.66,311.13,587.33,622.25]#D-D#
    nDict['e']=[20.60,41.20,82.4,164.81,329.63,659.25]#E
    nDict['f']=[21.83,23.12,43.65,46.25,87.31,92.50,174.61,185.00,349.23,
                369.99,698.46,739.99]#F-F#
    nDict['g']=[24.50,25.96,49.00,51.91,98.00,103.83,196.00,207.65,392.00,
                415.30,783.99,830.61]#G-G#
    nDict['a']=[27.50,29.14,55.00,58.27,110.00,116.54,220.00,233.08,440.00,
                466.16,880.00,932.33]#A-A#
    nDict['b']=[30.87,61.74,123.47,246.94,493.88,987.77]#B
    nDict['c1'] = [261.63,277.18,523.25,554.37,1046.50,1108.73]
    return nDict


def findNote(freq):
    nDict = noteDict()
    for key in nDict:
        for f in nDict[key]:
            if abs(f-freq)/f <= 0.05:
                return str(key)

   




