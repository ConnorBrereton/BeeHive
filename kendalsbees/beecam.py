#!/usr/bin/python

import tkinter

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

def keydown(event):
    if event.keysym == "Escape":
        root.destroy()
    char = event.char
    if char == "s":
        print("start")
        camera.start_preview()
        camera.brightness = 80
        camera.annotate_text = "Press 'e' to stop video"
        #sleep(10)
        #camera.stop_preview()
    elif char == "e":
        print("end")
        camera.capture('/home/pi/video.h264')
        #1.pack()
        sleep(5)
        camera.stop_recording()
        char = "n"
    else:
        print("Razduh")
        
root = tkinter.Tk()
print("begin")
root.bind_all('<key>', keydown)
w = tkinter.Label(root, text = "Press 'r' to Start Recording Video", font = ('Comic Sans', 36))

l = tkinter.Label(root, text = "Press 'e' to take a screenshot", font = ('Comic Sans', 36))

w.pack()
l.pack()
# root.withdraw()
root.mainloop()
