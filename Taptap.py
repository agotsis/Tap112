from __future__ import division,print_function
from visual import *

zLength = 50
border = 0
scene = display(title='Examples of Tetrahedrons',
     x=0, y=0, width=800, height=600,
     center=(0,0,0), background=(0,0,0))
sphere(pos = (0,0,-zLength),radius = 1, color = color.red)
cylinder(pos = (-21,0,zLength+border),axis = (-2,0,-zLength*10))
cylinder(pos = (21,0,zLength+border),axis = (2,0,-zLength*10))
box(pos = (0,0,zLength+border),length = 50,height = 1,width = 1)

noteScale = dict("C": -17.5,"D":-12.5,"E":-7.5,"F":-2.5,"G":2.5,"A":7.5,"B":12.5,"C":17.5]

def generateNote(note):
    t1 = sphere(pos=(noteScale[note],0,-zLength*5),radius=1,color=color.green)
    t1.visible = True
    notes.add(t1)

def checkBorderLine(notes):
    global zLength
    for note in notes:
        #print(note.pos.z)
        if note.pos.z > zLength+10:
            note.visible = False
            return notes.discard(note)
### Pause ###

def moveNotes(notes,vel,dt):
    if(len(notes) != 0):
        for note in notes:
            note.pos.z += vel * dt

def keyPressed(evt):
    global pause
    if (evt.key == "a"):
        

scene.autoscale=False
scene.userzoom = False
scene.userspin = False
scene.range = zLength

myFrame = frame()
scene.forward = scene.forward.rotate(angle=-0.2, axis=(1,0,0))
#myFrame.rotate(axis = (0,0,1), angle = 1.5682524)

notes = set()

zVelocity=150
t=0
dt=0.001
advance = True
pause = False

scene.bind("keydown",keyPressed)

### Advancing and deleting the text ###
while advance:
    rate(500)
    if not pause:
        moveNotes(notes,zVelocity,dt)
        checkBorderLine(notes)
        #print(diff_angle((1,0,0),scene.forward))
        if(len(notes) ==0):
            generateNotes()
            #pause = True
            #print("DONE")
        t += dt
    #zBound = scene.mouse.camera.z - (2/tan(scene.fov/2))
    """
    if (t1.pos.z > zBound):
        for obj in myFrame.objects:
            obj.visible = False
            del obj
        advance = not advance"""
