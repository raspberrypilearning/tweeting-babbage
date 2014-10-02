# Tweeting Babbage

Make a Babbage Bear that takes photos and sends tweets!

## Requirements

As well as a Raspberry Pi with an SD card loaded with Raspbian, you'll also need:

### Hardware

- 1 x [Raspberry Pi camera module](http://www.raspberrypi.org/product/camera-module/)
- 1 x Solderless breadboard (e.g. from [Pimoroni](http://shop.pimoroni.com/products/colourful-mini-breadboard))
- 2 x Male-to-female jumper leads (e.g. from [Pimoroni](http://shop.pimoroni.com/products/jumper-jerky))
- 1 x Tactile button (e.g. from [RS Components](http://uk.rs-online.com/web/p/tactile-switches/7182443/))

### Software

- python3-picamera
- python3-twython

See more information on checking you have these packages installed, and how to install them on the [software installation](software.md) page.

### Extras

- Babbage Bear from the [Swag Store](http://swag.raspberrypi.org/products/babbage-bear)

## Worksheet & included files

You'll need the worksheet for the instructions and the GPIO diagram for the button setup. Optionally, you can download the final version of the code to save typing it out.

- [The worksheet](worksheet.md)
- [GPIO diagram](images/gpio-setup.png)
- (Optional) Final version of Python code [babbage.py](code/babbage.py)
    - Download to the home directory with `wget http://goo.gl/????? -O babbage.py --no-check-certificate`

## Python 2 compatibility

This worksheet works fine in both Python 2 and Python 3. Python 3 is recommended but if you require Python 2 for an extension of the worksheet, simply use the equivalent Python 2 packages when installing. See the [software installation](software.md) page.

## Licence

Unless otherwise specified, everything in this repository is covered by the following licence:

[![Creative Commons Licence](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

***Tweeting Babbage*** by the [Raspberry Pi Foundation](http://www.raspberrypi.org) is licensed under a [Creative Commons Attribution 4.0 International Licence](http://creativecommons.org/licenses/by-sa/4.0/).

Based on a work at https://github.com/raspberrypilearning/tweeting-babbage
