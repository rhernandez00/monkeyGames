import pygame
import RPi.GPIO as GPIO

playing = -1
input1 = 16
input2 = 20
input3 = 21
input4 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(input1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(input2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(input3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(input4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(input1, GPIO.RISING)
GPIO.add_event_detect(input2, GPIO.RISING)
GPIO.add_event_detect(input3, GPIO.RISING)
GPIO.add_event_detect(input4, GPIO.RISING)
GPIO.add_event_callback(input1, pygame.mixer.music.playPause)

GPIO.add_event_callback(input2, pygame.mixer.music.pause)
GPIO.add_event_callback(input3, pygame.mixer.music.unpause)
GPIO.add_event_callback(input4, pygame.mixer.music.rewind)

def playPause():
    global playing
    if playing == -1:
        pygame.mixer.music.play()
        playing = 1
    elif playing == 1:
        pygame.mixer.music.pause()
        playing = 0
    else:
        pygame.mixer.music.unpause()
        playing = 1

pygame.mixer.init()
pygame.mixer.music.load("test.wav")




