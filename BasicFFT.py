import time

time0 = time.time()

import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

np.set_printoptions(threshold=np.nan)

rate, data = wavfile.read("420+700Hz.wav")

def almostEquals(a,b):
    return abs(a-b)<10**-3

N = len(data)
freqSpacing = rate/N

yf = scipy.fftpack.fft(data)

xf = np.linspace(0,rate//2,N//2)
'''
absolute = np.absolute(fft)
oneDimensional = np.ndarray.flatten(absolute)
amplitude = max(oneDimensional)
'''
absolute = np.abs(yf[:N//2])

fig, ax = plt.subplots()
ax.plot(xf,2.0/N*absolute)

maxAmplitude = np.amax(absolute,axis=0)

peakIndex = np.argwhere(abs(absolute-maxAmplitude)<(0.05*maxAmplitude))

freq = freqSpacing*peakIndex

time1 = time.time()

print(time1-time0)
print(peakIndex)
print(absolute[420/freqSpacing]-absolute[700/freqSpacing])
print(freq)
