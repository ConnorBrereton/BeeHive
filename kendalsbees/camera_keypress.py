#!/usr/bin/python

from picamera import PiCamera
from time import sleep

import pygame, sys
import pygame.locals

camera = PiCamera()
camera.rotation = 180
camera.start_preview()
camera.brightness = 80
sleep(5)
camera.stop_preview()

pygame.init()
BLACK = (0,0,0)
WIDTH = 1280
HEIGHT = 1024
windosSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

windowSurface.fill(BLACK)

while True:
    event = pygame.event.get()
    for event in events:
        if event.key == pygame.K_p:
        
            camera.stop_preview()
            pass
        if event.key == pygame.K_q:
            pygame.quit()
            sys.exit