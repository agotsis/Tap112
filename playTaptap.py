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
