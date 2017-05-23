# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:06:21 2017

@author: Raul
"""

from os import listdir
from os.path import isfile, join

soundPath = r'D:\monkeyGames\sounds'
soundType = '\calls'

myPath = soundPath + soundType
onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
onlyfiles