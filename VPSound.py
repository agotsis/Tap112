from __future__ import division,print_function
import pyaudio
import pygame
import time

def playsound(soundFilePath):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(soundFilePath)
    length = sound.get_length()
    time.clock()
    pygame.mixer.Sound.play(sound)
    while time.clock()<length:
        pass
    pygame.mixer.sound.stop()
    




