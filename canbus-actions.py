import serial, time, uinput

# PySerial can be Downloaded from this Link if needed
#https://pypi.python.org/pypi/pyserial


# ==== Serial Port Config ====
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/ttyUSB0'
# "ser.port = X-1" if using windows, where X is the number of the COM-port, -1 is because the .port function counts from 0 and not 1 like the com names in windows
ser.timeout = 10 # Specify the TimeOut in seconds, so that SerialPort doesn't hangs
ser.open() # Opens SerialPort

# ==== Keyboard buttons configurations ====
device = uinput.Device([
        uinput.KEY_NEXTSONG,
        uinput.KEY_PREVIOUSSONG,
        uinput.KEY_PLAYPAUSE,
        uinput.KEY_VOLUMEUP,
	    uinput.KEY_VOLUMEDOWN,
	    uinput.KEY_MUTE,
        uinput.KEY_M,
        uinput.KEY_O,
    ])

# Check if the connection is open
while not ser.isOpen():
    print('Could not connect to Serialport ' + ser.portstr)
    time.sleep(1)
print('Success! Opened Serial Connection with ' + ser.portstr)


while True:

    msg = ser.readline() #Read from Serial Port

    # Here are a list of supported keys that can be pressed using uinput
    # https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h#L74

    # Open Auto supported buttons
    # https://github.com/f1xpl/openauto/wiki/Keyboard-button-bindings

    msg = msg.decode("utf-8") # Converting from bytes to string
    msg = msg.strip() # Removing weird character like 

    if msg != False: # Do nothing if no new message
        if msg == "SIDE-UP":
            device.emit_click(uinput.KEY_NEXTSONG) # Next Track
        elif msg == "SIDE-DOWN":
            device.emit_click(uinput.KEY_PREVIOUSSONG) # Previous Track
        elif msg == "UP":
            device.emit_click(uinput.KEY_PLAYPAUSE) # Play/Pause Music
        elif msg == "DOWN":
            device.emit_click(uinput.KEY_MUTE) # Mute Volume
        elif msg == "VOLUME-UP":
            device.emit_click(uinput.KEY_VOLUMEUP) # Increase Volume
        elif msg == "VOLUME-DOWN":
            device.emit_click(uinput.KEY_VOLUMEDOWN) # Decrease Volume
        elif msg == "VOICE":
            device.emit_click(uinput.KEY_M) # Trigger the google assistant on openauto
        elif msg == "PHONE":
            device.emit_click(uinput.KEY_O) # Trigger a call to end on openauto

    # Print raw message for debugging
    print(msg) # Print What is Read from Port