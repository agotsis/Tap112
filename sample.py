from __future__ import division,print_function
from visual import *


def init(data):
    data.notes = []
    data.indexTrack = 0
    data.zVelocity=10
    data.t = 0
    data.dt = 0.001
    data.pause = False

def generateNotes(data):
    for i in xrange(-1,2):
        data.notes.append(sphere(frame=myFrame, pos=(5*i,0,-10),radius = 0.5,color = color.white))

def main():
    while advance:
    rate(500)
    if not pause:
        myFrame.pos.z += zVelocity*d
        t += dt
    zBound = scene.mouse.camera.z - (2/tan(scene.fov/2))
    """
    if (t1.pos.z > zBound) or (len(regText)==0):
        for obj in myFrame.objects:
            obj.visible = False
            del obj
        advance = not advance"""
### Pause ###

def keyPressed(evt):
    global pause
    if (evt.key == "p" or
        evt.key == "P") and evt.ctrl:
        pause = not pause


def main():
    class Struct(object): pass
    data = Struct()
    init(data)
    data.myFrame = frame()
    scene.autoscale=True
    scene.bind("keydown",keyPressed)
main()