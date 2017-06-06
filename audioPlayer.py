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

inputs = [16,20,21,26]

def playPause(inputVal):    
    global inputs
    global playing    
    global currentChannel
    global currentNum
    channel = inputs.index(inputVal)
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

GPIO.setmode(GPIO.BCM)
for i in inputs:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#setup
    GPIO.add_event_detect(i, GPIO.RISING) #event listeners

#event callbacks
GPIO.add_event_callback(inputs[0], playPause)
GPIO.add_event_callback(inputs[1], playPause)
GPIO.add_event_callback(inputs[2], playPause)
GPIO.add_event_callback(inputs[3], stopSound)


path = os.path.dirname(numpy.__file__)

soundPath = r'/home/pi/Desktop/monkeyGames/sounds'
soundType = ['/calls','/generated','/human',]
playing = False
currentChannel = 0
currentNum = 0


pygame.mixer.init() #win


