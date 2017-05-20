import pygame
import RPi.GPIO as GPIO

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
GPIO.add_event_callback(input1, pygame.mixer.music.play)
GPIO.add_event_callback(input2, pygame.mixer.music.pause)
GPIO.add_event_callback(input3, pygame.mixer.music.unpause)
GPIO.add_event_callback(input4, pygame.mixer.music.rewind)


pygame.mixer.init()
pygame.mixer.music.load("test.wav")




