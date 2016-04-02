from __future__ import division,print_function
from visual import *
import copy

zLength = 50
border = 0
scene = display(title='Examples of Tetrahedrons',
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
noteScale = {"C": [-17.5,color.white],"D":[-12.5,color.blue],"E":[-7.5,color.white],"F":[-2.5,color.blue],"G":[2.5,color.white],"A":[7.5,color.blue],\
             "B":[12.5,color.white],"C1":[17.5,color.blue]}
Master = copy.deepcopy(noteScale)
keysticks = dict()

for note in ["C","D","E","F","G","A","B","C1"]:
    x = noteScale[note][0]
    t1 = box(pos=(x,-1,zLength-7.5),size = (4,1,15),radius=1,color=noteScale[note][1])
    t1.visible = True
    keysticks[note] = t1

def drawKeyBoard():
    global noteScale
    global zLength

    for note in ["C","D","E","F","G","A","B","C1"]:
        x = noteScale[note][0]
        t1 = box(pos=(x,-1,zLength-7.5),size = (4,1,15),radius=1,color=noteScale[note][1])
        t1.visible = True

def drawRoad():
    global noteScale
    global zLength
    index = 0
    k = ["C","D","E","F","G","A","B"]
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

def generateNote():
    global note
    global notes
    if(len(note) != 0):
        x = Master[note][0]
        t1 = sphere(pos=(x,0,-zLength*5),radius=1,color=color.green)
        t1.visible = True
        if(note not in notes):
            notes[note] = [t1]
        else:
            notes[note].append(t1)

def checkBorderLine(notes):
    global zLength
    for note in notes:
        for i in range(len(notes[note])):
            pt = notes[note][i]
            if pt.pos.z > zLength+10:
                pt.visible = False
                notes[note].pop(i)
                return
            
def moveNotes(vel,dt):
    global notes
    if(len(notes) != 0):
        for note in notes:
            for i in range(len(notes[note])):
                pt = notes[note][i]
                pt.pos.z += vel * dt
pressed = True
def keyPressed(evt):
    global note
    if (evt.key == "a" or evt.key =="A"):
        note = "C"
    elif (evt.key == "s" or evt.key =="S"):
        note = "D"
    elif (evt.key == "d" or evt.key =="D"):
        note = "E"
    elif (evt.key == "f" or evt.key =="F"):
        note = "F"
    elif (evt.key == "j" or evt.key =="J"):
        note = "G"
    elif (evt.key == "k" or evt.key =="K"):
        note = "A"
    elif (evt.key == "l" or evt.key =="L"):
        note = "B"
    elif (evt.key == ";"): note = "C1"
    pressKey()

def keyReleased():
    global note
    global keysticks
    global Master
    if(len(note) > 0):
        for n in ["C","D","E","F","G","A","B","C1"]:
            keysticks[n].color = Master[n][1]
        note = ""  

def pressKey():
    global note
    global noteScale
    global keysticks
    global kt
    global dt
    if(note in "CDEFGABC1"):
        if(len(note) > 0):
            keysticks[note].color = color.green
            generateNote()

def checkHit():
    global notes
    global note
    global keynotes
    
    for no in notes:
        if(len(note) != 0):
            for i in range(len(notes[no])):
                pt = notes[no][i]
                if(no == note and (zLength-3 >= pt.pos.z >= zLength-12)):
                    pt.visible = False
                    score += 1
                    notes[note].pop(i)
                    drawScore()
                    return                   
score = 0
scoretext = text(text=str(score), pos = (40,50,0),
    align='center', depth=-0.3, color=color.green)

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
note = ""
zVelocity=150
t=0
kt = 0
dt=0.001
advance = True
pause = False

scene.bind("keydown",keyPressed)
scene.bind("keyup",keyReleased)

### Advancing and deleting the text ###
while advance:
    rate(500)
    if not pause:
        moveNotes(zVelocity,dt)
        checkHit()
        checkBorderLine(notes)
        if(len(notes) ==0):
            pass
        t += dt
        kt += dt
    #zBound = scene.mouse.camera.z - (2/tan(scene.fov/2))
    """
    if (t1.pos.z > zBound):
        for obj in myFrame.objects:
            obj.visible = False
            del obj
        advance = not advance"""

"""
http://www.twitrcovers.com/wp-content/uploads/2014/02/Super-Mario-l.jpg


"""



