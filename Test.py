import scipy.io.wavfile as wavfile
from BasicFFT import basicFFT

rate,data = wavfile.read("bin/420+700Hz.wav")

print(basicFFT(rate,data))