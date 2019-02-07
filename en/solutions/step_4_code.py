from picamera import PiCamera
from datetime import datetime
from time import sleep
from gpiozero import Button

camera = PiCamera()
button = Button(14)

now = datetime.now()
filename = ''

def take_photo():
    global filename
    filename = "{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}.png".format(now)
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture("/home/pi/{0}".format(filename))
    camera.stop_preview()

button.when_pressed = take_photo
