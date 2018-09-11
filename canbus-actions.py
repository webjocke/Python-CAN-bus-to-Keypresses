import serial, pyautogui, time, re

# PySerial can be Downloaded from this Link if needed
#https://pypi.python.org/pypi/pyserial


# ==== Serial Port Config ====
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/cu.usbmodem1421'
# "ser.port = X-1" if using windows, where X is the number of the COM-port, -1 is because the .port function counts from 0 and not 1 like the com names in windows
ser.timeout = 10 # Specify the TimeOut in seconds, so that SerialPort doesn't hangs
ser.open() # Opens SerialPort


# Check if the connection is open
while not ser.isOpen():
    print('Could not connect to Serialport ' + ser.portstr)
    time.sleep(1)
print('Success! Opened Serial Connection with ' + ser.portstr)


while True:

    msg = ser.readline() #Read from Serial Port

    # Here are a list of supported keys that can be pressed using pyautogui
    # https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys

    msg = msg.decode("utf-8") # Converting from bytes to string
    msg = msg.strip() # Removing weird character like 

    if msg != False: # Do nothing if no new message
        if msg == "SIDE-UP":
            pyautogui.press("nexttrack") # Next Track
        elif msg == "SIDE-DOWN":
            pyautogui.press("prevtrack") # Previous Track
        elif msg == "UP":
            pyautogui.press("playpause") # Play/Pause Music
        elif msg == "DOWN":
            pyautogui.press("volumemute") # Mute Volume
        elif msg == "VOLUME-UP":
            print("HWHOWHO")
            pyautogui.press("volumeup") # Increase Volume
        elif msg == "VOLUME-DOWN":
            pyautogui.press("volumedown") # Decrease Volume
        elif msg == "VOICE":
            pyautogui.press("m") # Trigger the google assistant on openauto
        elif msg == "PHONE":
            pyautogui.press("o") # Trigger a call to end on openauto

    # Print raw message for debugging
    print(msg) # Print What is Read from Port
