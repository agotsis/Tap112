from __future__ import division,print_function
from visual import *
import copy
from VPSound import *
import thread
from freqToNoteList import freqToNoteList
from BasicFFT import *
import time
from scipy.io.wavfile import read

#setting our sound files
wavFile = "bin/SMB.wav"
msDelay = 75

travelDelay = 1750

#calculating notes from wav file
sampleRate,data = read(wavFile)
notesList = freqToNoteList(intervalFFT(sampleRate,data,msDelay))

#animations

zLength = 50
border = 0
scene = display(title='Taptap 112',
     x=0, y=0, width=800, height=600,
     center=(0,0,0), background=(0,0,0))

sphere(pos = (0,0,-zLength),radius = 1, color = color.red)
cylinder(pos = (-21,0,zLength),axis = (-2,0,-zLength*10))
cylinder(pos = (21,0,zLength),axis = (2,0,-zLength*10))
box(pos = (0,-0.5,zLength-5),length = 45,height = 0.5,width = 0.5)
box(pos = (0,-0.5,zLength-10),length = 40,height = 0.5,width = 0.5)

w = 21
width = 10
#keyboard = box(pos=(0,0,zLength),size=(10,1,1),axis=(1,0,0),color = color.white)
noteScale = {"c": [-17.5,color.white],"d":[-12.5,color.blue],"e":[-7.5,color.white],"f":[-2.5,color.blue],"g":[2.5,color.white],"a":[7.5,color.blue],\
             "b":[12.5,color.white],"c1":[17.5,color.blue]}
Master = copy.deepcopy(noteScale)
keysticks = dict()

for note in ["c","d","e","f","g","a","b","c1"]:
    x = noteScale[note][0]
    t1 = box(pos=(x,-1,zLength-7.5),size = (4,1,15),radius=1,color=noteScale[note][1])
    t1.visible = True
    keysticks[note] = t1

def drawKeyBoard():
    global noteScale
    global zLength

    for note in ["c","d","e","f","g","a","b","c1"]:
        x = noteScale[note][0]
        t1 = box(pos=(x,-1,zLength-7.5),size = (4,1,15),radius=1,color=noteScale[note][1])
        t1.visible = True

def drawRoad():
    global noteScale
    global zLength
    index = 0
    k = ["c","d","e","f","g","a","b"]
    for i in range(len(k)):
        note = k[i]
        x = noteScale[note][0]
        t1 = box(pos=(x+2.5,-1.2+index,-zLength*3),size = (1,1,zLength*10),radius=1,color=(0.5,0.5,0.5))
        t1.visible = True
        if(i > 2):
            index += 1
        else:
            index -= 1
drawRoad()
scene.lights =[distant_light(direction=(0.5,0.5,0.2))]

#T0
def generateNote(note):
    #note is a string of either "a","b","c",etc.
    global notes
    global notes_lock
    with notes_lock:
        if(len(note) != 0):
            x = Master[note][0]
            t1 = sphere(pos=(x,0,-zLength*5),radius=1,color=color.green)
            t1.visible = True
            if(note not in notes):
                notes[note] = [t1]
            else:
                notes[note].append(t1)

def generateNotesFromList(notesList,msDelay):
    for chord in notesList:
        #chord is a list of notes
        chord = set(chord)
        for note in chord:
            if note != None:
                generateNote(note)
        time.sleep(msDelay/1000)
                

def checkBorderLine(notes):
    global zLength
    for note in notes:
        for i in range(len(notes[note])):
            pt = notes[note][i]
            if pt.pos.z > zLength+10:
                pt.visible = False
                del pt
                notes[note].pop(i)
                return

# T1           
def moveNotes(vel,dt):
    global notes
    global notes_lock
    with notes_lock:
        if(len(notes) != 0):
            for note in notes:
                for i in range(len(notes[note])):
                    pt = notes[note][i]
                    pt.pos.z += vel * dt
                
pressed = True
def keyPressed(evt):
    global note
    if (evt.key == "a" or evt.key =="a"):
        note = "c"
    elif (evt.key == "s" or evt.key =="S"):
        note = "d"
    elif (evt.key == "d" or evt.key =="d"):
        note = "e"
    elif (evt.key == "f" or evt.key =="f"):
        note = "f"
    elif (evt.key == "j" or evt.key =="J"):
        note = "g"
    elif (evt.key == "k" or evt.key =="K"):
        note = "a"
    elif (evt.key == "l" or evt.key =="L"):
        note = "b"
    elif (evt.key == ";"): note = "c1"
    pressKey()

def keyReleased():
    global note
    global keysticks
    global Master
    if(len(note) > 0):
        for n in ["c","d","e","f","g","a","b","c1"]:
            keysticks[n].color = Master[n][1]
        note = ""  

def pressKey():
    global note
    global noteScale
    global keysticks
    global kt
    global dt
    if(note in "cdefgabc1"):
        if(len(note) > 0):
            keysticks[note].color = color.green

def checkHit():
    global notes
    global note
    global keynotes
    global score
    for no in notes:
        if(len(note) != 0):
            for i in range(len(notes[no])):
                pt = notes[no][i]
                if(no == note and (zLength-3 >= pt.pos.z >= zLength-12)):
                    pt.visible = False
                    #score += 1
                    del pt
                    notes[note].pop(i)
                    #drawScore()
                    return                   
score = 0
#scoretext = text(text=str(score), pos = (40,50,0),
  #  align='center', depth=-0.3, color=color.green)

def drawScore():
    global score 
    scoretext.text = str(score)

scene.autoscale=False
scene.userzoom = False
scene.userspin = False
scene.range = zLength

myFrame = frame()
scene.forward = scene.forward.rotate(angle=-0.2, axis=(1,0,0))

notes = dict()
notes_lock = thread.allocate_lock()
note = ""
zVelocity=150
t=0
kt = 0
dt=0.001
advance = True
pause = False

scene.bind("keydown",keyPressed)
scene.bind("keyup",keyReleased)

thread.start_new_thread(generateNotesFromList,(notesList,msDelay))

counter = 0
### Advancing and deleting the text ###
while advance:
    rate(500)
    if not pause:
        counter +=1
        moveNotes(zVelocity,dt)
        checkHit()
        checkBorderLine(notes)
        t += dt
        if counter==travelDelay:
            thread.start_new_thread(playsound,(wavFile,))
    #zBound = scene.mouse.camera.z - (2/tan(scene.fov/2))


    

"""
http://www.twitrcovers.com/wp-content/uploads/2014/02/Super-Mario-l.jpg


"""



