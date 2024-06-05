import serial

ser = serial.Serial(port='/dev/ttyACM', baudrate=9600)


def LED_ON():
    ser.write(b'on')


def LED_OFF():
    ser.write(b'off')


def LED_BLINK():
    ser.write(b'blink')


def LED_STATUS():
    ser.write(b'status')
    value = ser.readline()
    valueString = str(value, 'UTF-8')
    print("LED: " + valueString.strip())


while True:
    command = input("Type your arduino command: ")
    if command == "on":
        LED_ON()
    elif command == "off":
        LED_OFF()
    elif command == "blink":
        LED_BLINK()
    elif command == "status":
        LED_STATUS()
