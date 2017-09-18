## Taking and saving a picture with PiCamera

The first stage of this project will be taking a picture with the help of the `PiCamera` module and saving the image file on your Raspberry Pi using a timestamp as a file name.

So to begin with your program should do the following:

1. Take a photo using the `PiCamera` module
1. Save the photo using a timestamp as the file name

Below are instructions detailing how to use the Raspberry Pi Camera Module, and how to get timestamps in Python. See if you can use this information to take pictures and name your image files with timestamps.

[[[rpi-picamera-connect-camera]]]

[[[rpi-picamera-take-photo]]]

[[[generic-python-timestamps]]]

--- hints --- --- hint ---
It might help to break this problem down into smaller parts, to see if it's easier to tackle.
1. Import the `PiCamera`, `datetime,` and `time` modules
1. Create a `camera` object
1. Create a preview
1. Create a string for the current timestamp
1. Take a picture and save it using timestamp string
1. Close the camera
--- /hint --- --- hint ---
Here's some partially completed code, with comments explaining what needs adding in to help you with the task:
```python
## Import the modules
from picamera import PiCamera()
from datetime import datetime
from time import sleep

## Set up the camera (you need to complete this)
camera =

## Get the current datetime stamp (you need to complete this)
now = datetime.now()
filename = "CODE FOR STRING FORMATTING HERE".format(now)

## Take the picture with a preview (you need to complete this)

## Close the camera
camera.close()

```
--- /hint --- --- hint ---
![pic with time stamp](images/pic_with_time_stamp.gif)
--- /hint --- --- /hints ---


