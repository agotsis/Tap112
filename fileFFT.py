import scipy.io.wavfile as wavfile
from BasicFFT import basicFFT, intervalFFT

#function takes in filename, returns list of frequencies for every specified interval

def fileFFT(filename,interval):
    rate,data = wavfile.read(filename)
    arrayList = intervalFFT(rate,data,interval)
    result = []
    for array in arrayList:
        result.append(list(array))
    return result