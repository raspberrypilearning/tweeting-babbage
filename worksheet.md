# Tweeting Babbage

Make a Babbage Bear that takes photos and sends tweets!

## Create a Twitter Account

First we need to create a Twitter account to use for the project.

1. Create a Twitter account for your Babbage Bear at [twitter.com](https://twitter.com)

    ![](images/create-twitter.png)

You might also want to upload a photo and fill out the bio.

## Create a Twitter Application

We need to register our application with Twitter to get keys which allow us to access the Twitter account from Python using the Twitter API (Application Programming Interface).

1. Go to [apps.twitter.com](https://apps.twitter.com) and click the **Create New App** button.

    ![](images/create-new-app.png)

1. Complete the application details form. You must enter an application name, description, website (this can be `http://www.raspberrypi.org` if you don't have one). Leave the Callback URL field blank and proceed.

1. Modify your app permissions from **Read only** to **Read and write**.

    ![](images/read-and-write.png)

1. Click the 'Keys and Access Tokens' tab and create an access token.

    ![](images/create-access-token.png)

1. Once you've clicked the **Create an Access Token** button, refresh the page and you'll see a new section beneath the **Application Settings** with your access token details.

1. You should now be able to see your **Consumer key**, **Consumer secret**, **Access token** and **Access token secret**. You'll need these four keys to connect to your Twitter account from your Python code. Don't share these keys with anyone as they can be used (without the account's password). If you share your code online, make sure not to include these keys. If you ever accidentally share or publish these keys, you should regenerate the keys at [apps.twitter.com](https://apps.twitter.com).

![](images/twitter-keys.png)

## Connect to Twitter from Python

Before we perform surgery on Babbage and insert a camera up his rear end, let's get the code doing what we want it to.

1. Boot your Raspberry Pi to the Desktop and launch `LXTerminal`

1. Because the Raspberry Pi doesn't have a real-time clock, we must start by setting the date on the system with the command:

    ```bash
    sudo date -s "2 OCT 2014 12:00:00"
    ```

    with the correct date. This is important as without the correct time we won't be able to connect to Twitter.

1. Create a folder for your project with the following command:

    ```bash
    mkdir tweeting-babbage
    ```

1. Enter this folder with `cd tweeting-babbage` and create the files we'll be using:

    ```bash
    touch auth.py babbage.py tweeting-babbage.py
    ```

1. Launch these Python files in `IDLE3` with root permissions (you'll need this for the GPIO) with the command:

    ```
    sudo idle3 *.py &
    ```

1. In `auth.py` paste your API keys from [apps.twitter.com](https://apps.twitter.com) in to variables like so:

    ```python
    consumer_key        = 'ABCDEFGHIJKLKMNOPQRSTUVWXYZ'
    consumer_secret     = '1234567890ABCDEFGHIJKLMNOPQRSTUVXYZ'
    access_token        = 'ZYXWVUTSRQPONMLKJIHFEDCBA'
    access_token_secret = '0987654321ZYXWVUTSRQPONMLKJIHFEDCBA'
    ```

1. Save `auth.py` and go to `babbage.py`. Import the `twython` library and the variables from `auth.py`:

    ```python
    from twython import Twython
    from auth import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )
    ```

1. Make a connection with the Twitter API using this set of keys:

    ```python
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )
    ```

1. Create a `main()` function which will be called when the script is run. We'll start with a basic "Hello world" tweet to test the connection works:

    ```python
    def main():
        message = "Hello world!"
        twitter.update_status(status=message)
    ```

    This uses the API's `update_status()` function to send a text tweet containing the text "Hello world!".

1. We'll also add an instruction at the end to run the `main()` method when the script is called directly:

    ```python
    if __name__ == '__main__':
        main()
    ```

    Your code should now look like this:

    ```python
    from twython import Twython
    from auth import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )

    def main():
        message = "Hello world!"
        twitter.update_status(status=message)
        print("Tweeted: %s" % message)

    if __name__ == '__main__':
        main()
    ```

1. Now save (`Ctrl + S`) and run with `F5`. You should see the message "Tweeted: Hello world!". Go to your Twitter profile in a web browser to verify it sent! This will be at `twitter.com/username` where `username` is your Twitter account's username.

![](images/twitter-hello-world.png)

Note that sending multiple tweets with the exact same text are classed as duplicates and rejected by Twitter. If you want to test it again, try tweeting a different message.

If you see an error, your API keys may be incorrect. Be sure to copy them exactly and check the spelling of the variables. Also check your Pi is online.

![](images/twitter-api-error.png)

## Tweet Random messages

Now we can send some text as a tweet, let's mix it up a bit.

1. First, import the random choice function:

    ```python
    import random.choice
    ```

    This function takes a list and returns a single entry at random.

1. Now create a list of messages like so:

    ```python
    messages = [
        "Hello world",
        "Hi there",
        "My name is Babbage",
        "What's up?",
        "How's it going?",
        "Have you been here before?",
        "Get a hair cut!",
        ]
    ```

1. Replace `message = "Hello world!"` with `message = random.choice(messages)`.

1. Run the code again two or more times to see different messages being tweeted at random.

## Tweet a picture

Now the Twitter connection has been tested, let's try to upload a picture. Rather than try to hook up the camera now we'll test it independently.

1. Find a picture, copy one to your Raspberry Pi or download one from the internet and save it to your home folder. Make a note of its location (something like `/home/pi/Downloads/image.jpg`).

    ![](images/file-manager-image.png)

1. Modify the `main()` function in the code accordingly:

    ```python
    message = "Hello world - here's a picture!"
    with open('/home/pi/Downloads/image.jpg', 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)
    ```

    Making sure to get full path to the image correctly.

    This opens the file and uses the `update_status_with_media()` function to upload the image along with the tweet text.

1. Run the code and see if it tweets the text and image together!

    ![](images/tweet-image.png)

## Take a picture with the Pi camera

Now we know we can upload a given picture to Twitter, let's take one with the Pi camera.

1. With the Pi switched off, connect the camera to the camera port.

    ![](images/connect-camera.png)

1. Boot the Pi and from the command line or LXTerminal, test it works with the command `raspistill -k`. If you see the camera's image on the screen, you know it's working. Press `Ctrl + C` to exit the preview.

1. Now open a new Python window in IDLE3, save as `camera.py` and enter the following code:

    ```python
    from picamera import PiCamera
    from time import sleep

    with PiCamera() as camera:
        camera.start_preview()
        sleep(3)
        camera.capture('/home/pi/image.jpg')
        camera.stop_preview()
    ```

    This is a test script to check we can take a picture from Python.

1. Run with `F5` and you should see a preview on the screen for 3 seconds before the camera takes the picture.

1. Open the file manager and you should see `image.jpg`. Double click the icon to open it up.

    ![](images/file-manager.png)

## Tweet a picture from the Pi camera

Now we'll copy the `picamera` code we just used to take a picture in to the `babbage.py` file to make it tweet the photo taken by the Pi camera.

1. First add the `import` lines at the top:

    ```python
    from picamera import PiCamera
    from time import sleep
    ```

    Imports are best kept at the top of the line before anything else.

1. Then add the `picamera` lines in the `main()` method:

    ```python
    with PiCamera() as camera:
        camera.start_preview()
        sleep(3)
        camera.capture('/home/pi/image.jpg')
        camera.stop_preview()

    message = "Here's a Pi camera picture!"
    with open('/home/pi/image.jpg', 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)
    ```

1. Now run the code and it will save to `image.jpg` in the home folder and upload it to Twitter.

1. Check Twitter to see if it worked!

    ![](images/twitter-picamera.png)

## Use a timestamp

Now let's fix the hard-coded filename of `image.jpg` and use something more dynamic. It would be better to timestamp the filename so it will never get written over. And we should store it in a folder inside our project.

1. In the terminal window, create a new folder inside `twitter-babbage` called `photos` with `mkdir photos`.

1. Import the `datetime` function with `from datetime import datetime`.

1. Save the timestamp as a variable before taking the picture and pass this in to the path string:

```python
timestamp = datetime.now().isoformat()
photo_path = '/home/pi/tweeting-babbage/photos/%s.jpg' % timestamp
camera.capture(photo_path)
```

    The timestamp is formatted like `2014-10-02T05:10:25.642155`.

1. Also change the `update_status_with_media()` call with this new photo path:

```python
with open(photo_path, 'rb') as photo:
    twitter.update_status_with_media(status=message, media=photo)
```

1. Run the code again and it should save the image in the `tweeting-babbage/photos` folder and tweet it as usual.

## Wire up a GPIO button

Now we'll add a hardware button that we'll use to trigger the camera.

1. Connect the button to the breadboard and wire it up to Ground and GPIO 17 like so:

    ![](images/gpio-diagram.png)

1. Return to the `camera.py` script to test it out. First import the GPIO library at the top:

    ```python
    import RPi.GPIO as GPIO
    ```

1. Then add some lines between the imports and the main code to set up the GPIO pins:

    ```python
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)
    ```

    This configures the code to use the Broadcom (`BCM`) pin numbering system (as opposed to `BOARD`) and sets up GPIO pin 17 as an input.

1. Now just add the button press trigger before taking the picture. It should go between `start_preview()` and `capture()` - you can remove the `sleep()`:

    ```python
    camera.start_preview()
    GPIO.wait_for_edge(17, GPIO.FALLING)
    camera.capture(photo_path)
    ```

    `GPIO.wait_for_edge()` is the trigger. It means "wait for an input on pin 17". The code will pause on that line until it receives a button press.

1. Run the code and you should see a preview of the camera picture. When you press the button it should take a picture and exit the preview.

![](images/gpio-setup.png)

If your button press has no effect, make sure your button is wired up correctly and to the correct pins. If you can't get it to work try pressing `Ctrl + C` while pressing the button to try to force an exit.

## Put it all together

Now we've got the button triggering the camera and we know we can tweet pictures taken with the camera, let's put it all together in `babbage.py`.

1. Add the GPIO library import and GPIO setup lines to the top.

1. Add the `wait_for_edge()` line before the capture. You probably want to leave the `sleep()` in this time.

1. Press the button when the preview appears, and it should tweet the picture from the camera.

## Final code

Your final code should look something like this:

```python
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
```

But feel free to make any modifications you see fit!

## Tweeting Babbage

Now we have the code doing exactly what we want, let's put it in to action (or in to Babbage, to be more precise).
