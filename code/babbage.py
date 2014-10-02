from twython import Twython
from picamera import PiCamera
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
import random.choice
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

messages = [
    "Hello world",
    "Hi there",
    "My name is Babbage",
    "What's up?",
    "How's it going?",
    "Have you been here before?",
    "Get a hair cut!",
    ]

def main():
    message = random.choice(messages)

    with PiCamera() as camera:
        camera.start_preview()
        GPIO.wait_for_edge(17, GPIO.FALLING)
        timestamp = datetime.now().isoformat()
        photo_path = '/home/pi/tweeting-babbage/photos/%s.jpg' % timestamp
        sleep(3)
        camera.capture(photo_path)
        camera.stop_preview()

    with open(photo_path, 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)

if __name__ == '__main__':
    main()
