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

--- hints ---
--- hint ---
Here's a video showing you how it's all done:
<iframe width="560" height="315" src="https://www.youtube.com/embed/lQD3csZ4E8k" frameborder="0" allowfullscreen></iframe>
--- /hint ---
--- /hints ---


- The final thing to do is to set up your Raspberry Pi so that the `tweeting_babbage.py` program starts automatically whenever the Pi is booted up.

[[[nix-bash-crontab]]]
