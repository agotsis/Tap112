<<<<<<< HEAD
import thread
import time
from fileFFT import fileFFT
from PlaySound import AudioFile

def playTaptap(filename):
    freqList = fileFFT(filename)
    a = AudioFile(filename)
    def playSound(a):
        #timerdelay here
        a.play()
        #timerdelay here
        a.close()
    try:
        thread.start_new_thread(VPythonfunction,(freqList))
        thread.start_new_thread(playSound(a))
    except:
        print("Error: unable to start thread!")
=======
import scipy.io.wavfile as wavfile
from BasicFFT import maxFFT, intervalFFT

rate,data = wavfile.read("bin/mixedTest.wav")

print(intervalFFT(rate,data,250))

rate,data = wavfile.read("bin/420+700Hz.wav")

print(maxFFT(rate,data))
>>>>>>> FFT
