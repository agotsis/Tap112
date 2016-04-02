import numpy as np
import scipy.fftpack

def basicFFT(rate,arrayData):
    #takes in data from wavfile.read("fileName.wav")
    N = len(arrayData)
    freqSpacing = rate/N
    rawFFT = scipy.fftpack.fft(arrayData)
    positiveFreqs = np.abs(rawFFT[:N//2])
    maxAmplitude = np.amax(positiveFreqs,axis=0)
    epsilon = 0.05*maxAmplitude
    peakIndex = np.argwhere(abs(positiveFreqs-maxAmplitude)<epsilon)
    freq = freqSpacing*peakIndex
    return freq.flatten()