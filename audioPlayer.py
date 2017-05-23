# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:06:21 2017

@author: Raul
"""

from os import listdir
from os.path import isfile, join
import pygame

import numpy, os
path = os.path.dirname(numpy.__file__)


soundPath = r'D:\monkeyGames\sounds'
soundType = ['\calls','\generated','\human',]
playing = False
currentChannel = 0
currentNum = 0



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
    pygame.mixer.music.load(soundFiles[nextNum])
    currentChannel = channel
    currentNum = nextNum
    pygame.mixer.music.play()
