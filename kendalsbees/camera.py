from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.start_preview()
camera.brightness = 80
sleep(20)
camera.stop_preview()