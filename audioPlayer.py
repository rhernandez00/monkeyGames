# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:06:21 2017

@author: Raul
"""

from os import listdir
from os.path import isfile, join
import pygame
import numpy, os
import RPi.GPIO as GPIO

input1 = 16
input2 = 20
input3 = 21
input4 = 26

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(input1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(input2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(input3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(input4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#event listeners
GPIO.add_event_detect(input1, GPIO.RISING)
GPIO.add_event_detect(input2, GPIO.RISING)
GPIO.add_event_detect(input3, GPIO.RISING)
GPIO.add_event_detect(input4, GPIO.RISING)
#event callbacks
GPIO.add_event_callback(input1, playPause)
GPIO.add_event_callback(input2, playPause)
GPIO.add_event_callback(input3, playPause)
GPIO.add_event_callback(input4, stopSound)


path = os.path.dirname(numpy.__file__)

soundPath = r'/home/pi/Desktop/monkeyGames/sounds'
soundType = ['/calls','/generated','/human',]
playing = False
currentChannel = 0
currentNum = 0


pygame.mixer.init() #win


def playPause(channel):
    
    global playing    
    global currentChannel
    global currentNum
    if playing:    
        pygame.mixer.music.stop()
    else:
        playing = True
    myPath = soundPath + soundType[channel]
    soundFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
    if currentChannel == channel:
        nextNum = currentNum + 1
        if nextNum >= len(soundFiles):
            nextNum = 0
    else:
        nextNum = 0
    fileToLoad = myPath + r'/' + soundFiles[nextNum]
    pygame.mixer.music.load(fileToLoad)
    currentChannel = channel
    currentNum = nextNum
    pygame.mixer.music.play()

def stopSound(channel):
    global playing    
    global currentChannel
    global currentNum
    if playing:    
        pygame.mixer.music.stop()
        playing = False        
    currentChannel = 0
    currentNum = 0