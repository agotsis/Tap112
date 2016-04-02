from __future__ import division,print_function
from visual import *
from PIL import Image
from PIL import _imaging


#http://vpython.org/contents/docs/materials.html

zLength = 50
border = 0
scene = display(title='Examples of Tetrahedrons',
     x=0, y=0, width=800, height=600,
     center=(0,0,0), background=(0,0,0))
name = "MarioBG"
im = Image.open(name + ".jpg")
im = im.resize((512,512),Image.ANTIALIAS)
materials.saveTGA(name,im)
data = materials.loadTGA(name)
mariobg = materials.texture(data = data, mapping = "rectangular", interpolate = False, mipmap = False)
#box(pos = (0,0,-2000),size = (5000,3000,1),material = materials.bricks)

sphere(pos = (0,0,-zLength),radius = 1, color = color.red)
cylinder(pos = (-21,0,zLength),axis = (-2,0,-zLength*10))
cylinder(pos = (21,0,zLength),axis = (2,0,-zLength*10))
#box(pos = (0,0,zLength),length = 50,height = 1,width = 1)
#box(pos = (0,0,zLength-15),length = 40,height = 1,width = 1)

w = 21
width = 10
#keyboard = box(pos=(0,0,zLength),size=(10,1,1),axis=(1,0,0),color = color.white)
noteScale = {"C": -17.5,"D":-12.5,"E":-7.5,"F":-2.5,"G":2.5,"A":7.5,"B":12.5,"C1":17.5}
def drawKeyBoard():
    global noteScale
    global zLength
    scale = 6
    index = 0
    c = color.white
    for note in noteScale:
        if(c == color.white):
            c = color.blue
        else:
            c = color.white

        index += 1
        x = noteScale[note]
        t1 = box(pos=(x,-1,zLength-7.5),size = (1*scale,0.3*scale,2*scale),radius=1,color=c)
        t1.visible = True

"""
    global w
    global width
    wKeya = box(pos=(-4*width,-5,0),size=(1,0.3,2),color=color.white)
    wKeys = box(pos=(-3*width,-5,0),size=(1,0.3,2),color=color.blue)
    wKeyd = box(pos=(-2*width,-5,0),size=(1,0.3,2),color=color.white)
    wKeyf = box(pos=(-1*width,-5,0),size=(1,0.3,2),color=color.blue)
    wKeyj = box(pos=(0*width,-5,0),size=(1,0.3,2),color=color.white)
    wKeyk = box(pos=(1*width,-5,0),size=(1,0.3,2),color=color.blue)
    wKeyl = box(pos=(2*width,-5,0),size=(1,0.3,2),color=color.white)
    wKey_ = box(pos=(3*width,-5,0),size=(1,0.3,2),color=color.blue) """  
drawKeyBoard()
scene.lights =[distant_light(direction=(0.5,0.5,0.2))]

pressedA = False
pressedS = False
pressedD = False
pressedF = False
pressedJ = False
pressedK = False
pessedL = False
pressed_ = False


def generateNote():
    global note
    if(len(note) != 0):
        x = noteScale[note]
        t1 = sphere(pos=(x,0,-zLength*5),radius=1,color=color.green)
        t1.visible = True
        notes.add(t1)
        note = ""

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
    global note
    if (evt.key == "a" or evt.key =="A"): note = "C"
    elif (evt.key == "s" or evt.key =="S"): note = "D"
    elif (evt.key == "d" or evt.key =="D"): note = "E"
    elif (evt.key == "f" or evt.key =="F"): note = "F"
    elif (evt.key == "j" or evt.key =="J"): note = "G"
    elif (evt.key == "k" or evt.key =="K"): note = "A"
    elif (evt.key == "l" or evt.key =="L"): note = "B"
    elif (evt.key == ";"): note = "C1"    
scene.autoscale=False
scene.userzoom = False
scene.userspin = True
scene.range = zLength

myFrame = frame()
scene.forward = scene.forward.rotate(angle=-0.2, axis=(1,0,0))
#myFrame.rotate(axis = (0,0,1), angle = 1.5682524)

notes = set()
note = ""
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
        generateNote()
        #print(diff_angle((1,0,0),scene.forward))
        if(len(notes) ==0):
            #generateNote(note)
            #pause = True
            #print("DONE")
            pass
        t += dt
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



