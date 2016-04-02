import scipy.io.wavfile as wavfile
from BasicFFT import basicFFT, intervalFFT

rate,data = wavfile.read("bin/mixedTest.wav")

print(intervalFFT(rate,data,250))

rate,data = wavfile.read("bin/420+700Hz.wav")

print(basicFFT(rate,data))