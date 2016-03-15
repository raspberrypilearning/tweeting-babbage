# Tweeting Babbage

Make a Babbage Bear that takes photos and sends tweets!

![Tweeting Babbage](cover.png)

## Requirements

As well as a Raspberry Pi with an SD card loaded with Raspbian, you'll also need:

### Hardware

- 1 x [Raspberry Pi camera module](http://www.raspberrypi.org/product/camera-module/)
- 1 x Set of Quick-Connect Wires (e.g. from [ModMyPi](https://www.modmypi.com/raspberry-pi-hacking/buttons-and-switchs/arcade-button-quick-connect-wires))
- 1 x Tactile button (e.g. from [ModMyPi](http://www.modmypi.com/raspberry-pi/hacking-and-prototyping/buttons-and-switches/colorful-tactile-button-switch-assortment-round-15-pack))

### Software

- GPIO Zero
- Twython

See more information on checking you have these packages installed, and how to install them, on the [software installation](software.md) page.

### Extras

- Babbage Bear from the [Swag Store](http://swag.raspberrypi.org/products/babbage-bear)
- Scissors
- Pliers
- Safety pins
- USB WiFi dongle (optional)

## Worksheet & included files

You'll need the worksheet for the instructions and the GPIO diagram for the button setup. Optionally, you can download the final version of the code to save typing it out.

- [The worksheet](worksheet.md)
- [GPIO diagram](images/gpio-diagram.png)
- (Optional) Final version of Python code [babbage.py](code/babbage.py) and [auth.py](code/auth.py)
    - Download to the home directory with:

        ```bash
        wget http://goo.gl/ySSbDl -O babbage.py --no-check-certificate
        wget http://goo.gl/msiYoo -O auth.py --no-check-certificate
        ```

## Licence

Unless otherwise specified, everything in this repository is covered by the following licence:

[![Creative Commons Licence](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

***Tweeting Babbage*** by the [Raspberry Pi Foundation](http://www.raspberrypi.org) is licensed under a [Creative Commons Attribution 4.0 International Licence](http://creativecommons.org/licenses/by-sa/4.0/).

Based on a work at https://github.com/raspberrypilearning/tweeting-babbage
