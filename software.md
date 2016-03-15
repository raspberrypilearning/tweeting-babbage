# Software installation

You'll need to make sure you have the following packages installed to proceed with the worksheet:

- GPIO Zero
- Twython
- Gnome Schedule

You'll need to be online to install packages.

First update and upgrade your system. Enter the following commands in to the terminal:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Now install the packages you'll need:

```bash
sudo apt-get install python3-gpiozero gnome-schedule
sudo pip3 install twython
```

Test you have everything you need by entering the following commands:

```bash
python3 -c "import gpiozero"
python3 -c "import twython"
```

This should bring you back to the command prompt with no errors. If you get an error saying `No module named X` then check you entered the commands above correctly.

You should also see a new item in the main menu for **Scheduled Tasks**.
