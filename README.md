# CAN-bus-to-Arduino-to-Raspberry-Pi-Python-Keyboard-Press
This is a part of my car project. Basically I want to be able to use the media buttons on my car's steering wheel and trigger stuff on my computer. More exact a Raspberry pi running Android Auto (Open Auto). Goal is to get a button for volume up, volume down, media play/pause and a trigger for voice commands.

## Dataflow
* A Arduino that listens on the CAN-bus. Filters the data and sends only the steering wheel actions out on the serial port.
* The python script listens for the data and makes a keypress on the computer for each invidual steering wheel action.
* Woops that list was really short, the flow is basically really easy.

## Components Needed - My Setup
* A Arduino Uno (Original, ATmega328p)
* Sparkfun CAN-bus Shield (Uses MCP2515, MCP2551)
* A Rasberry Pi running Raspbian (RPi 3 B+, RASPBIAN STRETCH WITH DESKTOP 2018-06-27 4.14)
* A Opel Astra H 2005, with MS-CAN, 95kbps, CAN-H Pin3, CAN-L Pin11

## How to run

#### Arduino Side
* Install the MCP-can library in the Arduino IDE.
* Copy the files in the lib-files/ into the downloaded library's folder, replacing the files that are there. (These are a bit modified)
* Open `canbus-reciver/canbus-reciver.ino` from this repo and changes the filter ID's for your cars component. The default is the onces for my steeringwheel.
* Upload the included sketch in this repository to your Arduino.

#### Computer Side
* Install Raspbian on your Raspberry Pi ([Raspbian Download](https://www.raspberrypi.org/downloads/raspbian/))
* Run `pip install pyautogui` in the terminal to install a needed library.
* Run `pip install pyserial` in the terminal to install another needed library.
* Run `pip install regex` in the terminal to install one more needed library.
* Open `canbus-actions.py` and change it to your likings. The default is to listen for my steering wheel buttons and press coresponding keys.
* Start the python script and/or make the script run at startup by typing `sudo echo "sudo python /path/to/canbus-actions.py &" >> /etc/rc.local` in the terminal. This should make the script start up on every boot.

## TODO:
* Make the traffic bidirectional so that the python script can request the Arduino to send out data on the CAN-bus when something is triggered on the computer.

## Special Thanks and Inspiration
* Info about my Opel Astra H's CAN-Bus from [vauxhallownersnetwork.co.uk](https://www.vauxhallownersnetwork.co.uk/index.php?threads/canbus-information-for-project.434211/)
* Help with the code from chukonu's github [repository](https://github.com/chukonu/astra-h-canbus-shield) and his [YouTube video](https://www.youtube.com/watch?v=GrgyPQrKCEU)