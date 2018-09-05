import serial, pyautogui, time

# PySerial can be Downloaded from this Link if needed
#https://pypi.python.org/pypi/pyserial


# ==== Serial Port Config ====
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/ttyUSB0'
# "ser.port = X-1" if using windows, where X is the number of the COM-port, -1 is because the .port function counts from 0 and not 1 like the com names in windows
ser.timeout = 10 # Specify the TimeOut in seconds, so that SerialPort doesn't hangs
ser.open() # Opens SerialPort


# Check if the connection is open
while not ser.isOpen():
    print 'Could not connect to Serialport ' + ser.portstr
    time.sleep(1)
print 'Success! Opened Serial Connection with ' + ser.portstr


while True:    

    msg = ser.readline() #Read from Serial Port

    # Here are a list of supported keys that can be pressed using pyautogui
    # https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys

    if msg == not False: # Do nothing if no new message
        if msg == "MEDIA-NEXT":
            pyautogui.press("nexttrack") # Next Track
        elif msg == "MEDIA-PREVIOUS":
            pyautogui.press("prevtrack") # Previous Track
        elif msg == "MEDIA-PLAYPAUSE":
            pyautogui.press("playpause") # Play/Pause Music
        elif msg == "MEDIA-VOLUMEUP":
            pyautogui.press("volumeup") # Increase Volume
        elif msg == "MEDIA-VOLUMEDOWN":
            pyautogui.press("volumedown") # Decrease Volume
        elif msg == "MEDIA-VOLUMEMUTE":
            pyautogui.press("volumemute") # Mute Volume
        elif msg == "MEDIA-VOICE":
            pyautogui.press("m") # Trigger the google assistant on openauto

    # Print raw message for debugging
    print 'RECIVED: ' + msg #Print What is Read from Port
