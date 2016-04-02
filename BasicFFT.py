from __future__ import division, print_function
import numpy as np
import scipy.fftpack

def basicFFT(rate, dataArray):
    N = len(dataArray)
    freqSpacing = rate/N
    rawFFT = scipy.fftpack.fft(dataArray)
    positiveFreqs = np.abs(rawFFT[:N//2])
    return positiveFreqs

def maxFFT(rate, dataArray):
    N = len(dataArray)
    freqSpacing = rate/N
    rawFFT = scipy.fftpack.fft(dataArray)
    positiveFreqs = np.abs(rawFFT[:N//2])
    maxAmplitude = np.amax(positiveFreqs,axis=0)
    epsilon = 0.05*maxAmplitude
    peakIndex = np.argwhere(abs(positiveFreqs-maxAmplitude)<epsilon)
    freq = freqSpacing*peakIndex
    return freq.flatten()

def intervalFFT(rate, dataArray, msInterval):
    samplesPerInterval = int(msInterval / 1000 * rate)
    N = len(dataArray)

    intervals = []
    for startIndex in range(0, N - samplesPerInterval, samplesPerInterval):
        intervals.append(dataArray[startIndex:startIndex+samplesPerInterval])

    frequencies = []
    for interval in intervals:
        frequencies.append(maxFFT(rate, interval))
    return frequencies