from __future__ import division,print_function
from visual import *

scene.autoscale=False

myFrame = frame()
regText = "Let's play typeracer!"
highText = ""
t1 = text(frame=myFrame,text=regText,align="center",height=1,depth=-0.2,
          pos=(0,-3,-10),color = color.white)
t1.visible = True
highlight = text(frame=myFrame,text=highText,align="left",depth = -0.2,
                 pos=(t1.pos.x-(t1.width/2),t1.pos.y,t1.pos.z),
                 color = color.yellow)
indexTrack = 0
zVelocity=10
t=0
dt=0.001

advance = True
pause = False

### Pause ###

def keyPressed(evt):
    global pause
    global regText
    global highText
    if (evt.key == "p" or
        evt.key == "P") and evt.ctrl:
        pause = not pause
    if len(regText)!=0:
        currChar = regText[0]
        if evt.key == currChar:
            highText+=currChar
            if len(regText)==1:
                regText=""
            else:
                regText=regText[1:]

scene.bind("keydown",keyPressed)

### Advancing and deleting the text ###
while advance:
    rate(500)
    if not pause:
        myFrame.pos.z += zVelocity*dt
        highlight.text = highText
        t += dt
    zBound = scene.mouse.camera.z - (2/tan(scene.fov/2))
    if (t1.pos.z > zBound) or (len(regText)==0):
        for obj in myFrame.objects:
            obj.visible = False
            del obj
        advance = not advance
