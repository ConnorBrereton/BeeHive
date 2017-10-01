from picamera import PiCamera
from time import sleep

import pygame
pygame.init()

print("Hello")

while True:
    events = pygame.event.get()
    print(events)
    for event in events:
        if event.key == pygame.K_p:
            print("start")
            pass
        if event.key == pygame.k_s:
            print("stop")
            pass