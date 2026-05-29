## Triggering a photo with a button

In this project, your Raspberry Pi will eventually end up being embedded inside your cuddly toy, so using a breadboard to wire up a button would be a little impractical. Instead you're going to connect it to the Pi with some quick-connect wires.

### Wiring your button

- Connect the button to the wires and attach it by clamping with a pair of pliers.
  ![button-wire-pliers](images/button-wire-pliers.jpg)

- Flatten the remaining two button feet.
  ![flatten-button-feet](images/flatten-button-feet.jpg)
  
- Wire it up to the ground pin and **GPIO 14** like so:
  ![gpio-diagram](images/gpio-diagram.png)
  
- With your camera connected, your finished setup should look something like this:

  ![gpio-camera-setup](images/gpio-camera-setup.jpg)

### Triggering the camera when the button is pressed

The `when_pressed` method for the `Button` class in `gpiozero` can be used to call any function you have written.

Your first step will be to create a new function called `take_photo`. Inside this function you should place code to get the timestamp, save it as a **global variable**, and take the photo. Then write code to call this function when the button is pressed. Have a look at the steps below if you are unsure about functions or triggering them with buttons.

[[[generic-python-simple-functions]]]

[[[rpi-python-function-calls-with-buttons]]]

--- hints ---
--- hint ---
Here's a video showing you how to write the code:
<iframe width="560" height="315" src="https://www.youtube.com/embed/CH1fstgfgrI" frameborder="0" allowfullscreen></iframe>
--- /hint ---
--- /hints ---





