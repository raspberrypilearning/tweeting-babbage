## Tweeting text and photos

The next step is to post your photo, along with an accompanying message, as a Twitter update.

**If you are under 13, you cannot sign up for a Twitter account, so you will need to use the account of a parent or guardian. Also, it is important to never share personal information or identifying photos on any social network if you are under 18.**

To achieve this, you'll need to make some changes to your script. Below is a list of the elements you'll need to add or change in your script.
You're going to want to edit you script so that:
- each time the button is pressed
- not only is the photo taken, but a random phrase is chosen from a list of phrases
- and the phrase and photo are sent to Twitter together.

Have a look at the information below to learn how to create a Twitter account and register an app, and post messages and images as status updates via a Python script.

- Here are instructions for registering your Twitter app:

[[[generic-api-registering-twitter]]]

- Here are instructions for sending a tweet using Python:

[[[generic-python-sending-a-tweet]]]

- Finally, here are instuctions on how to choose random items from a list:

[[[generic-python-random-choice]]]

--- hints --- --- hint ---
Your code should follow this structure:
1. Importing modules and creating objects
1. A function that takes and saves a photo
1. A funtion that posts a random phrase and photo to Twitter
1. A function that calls the previous two functions
1. A trigger that calls the third function when the button is pushed
--- /hint --- --- hint ---
Here's some partially completed code to help you along:
```python
from picamera import PiCamera
from datetime import datetime
from time import sleep
from gpiozero import Button
from random import choice
import tweepy
import json

btn = Button(14)
camera = PiCamera()

with open('twitter_auth.json') as file:
    secrets = json.load(file)

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

twitter = tweepy.API(auth)

status = [#Lots of different messages here]

filename = ''

def take_photo():
    global filename
	## code to get filename from timestamp
	## code to take a photo

def send_tweet():
	##code to send tweet

def go():
    take_photo()
    send_tweet()

btn.when_pressed = go
```
--- /hint --- --- hint ---
Here's a video showing you how it's all done:
<iframe width="560" height="315" src="https://www.youtube.com/embed/lQD3csZ4E8k" frameborder="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---

- The final thing to do is to set up your Raspberry Pi so that the `tweeting_babbage.py` program starts automatically whenever the Pi is booted up.

[[[nix-bash-crontab]]]
