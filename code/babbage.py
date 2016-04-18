from twython import Twython
from picamera import PiCamera
from time import sleep
from datetime import datetime
from gpiozero import Button
import random
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

button = Button(14)
camera = PiCamera()

messages = [
    "Hello world",
    "Hi there",
    "My name is Babbage",
    "What's up?",
    "How's it going?",
    "Have you been here before?",
    "Get a hair cut!",
]

while True:
    button.wait_for_press()
    message = random.choice(message)
    timestamp = datetime.now().isoformat()
    photo_path = '/home/pi/tweeting-babbage/photos/%s.jpg' % timestamp
    sleep(3)
    camera.capture(photo_path)

    with open(photo_path, 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)
