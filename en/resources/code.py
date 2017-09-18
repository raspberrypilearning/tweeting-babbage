from picamera import PiCamera
from datetime import datetime
from time import sleep
from gpiozero import Button
from random import choice
import tweepy
import json

btn = Button(17)
camera = PiCamera()

with open('twitterauth.json') as file:
    secrets = json.load(file)

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

twitter = tweepy.API(auth)

status = ['Hey there peeps',
          'Check out my photo',
          'Babbage is coming at ya']

filename = ''

def take_photo():
    global filename
    now = datetime.now()
    filename = "{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}.png".format(now)
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture("/home/pi/{0}".format(filename))
    camera.stop_preview()

def send_tweet():
    twitter.update_with_media('/home/pi/{0}'.format(filename), choice(status))

def main():
    take_photo()
    send_tweet()

btn.when_pressed = main
