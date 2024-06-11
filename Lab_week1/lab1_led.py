#   Students: Ryoma Nonaka & Jonas Skolnik
#   UvAnetID: 14932431 & 14932423
#   Studie: BSc Informatica
#   File: lab1_led.py
#   Goal: This file is used to give commands in the terminal
#   to the arduino. It contains the on, off, blink and status option.
#   after sending the command the arduino procceeds to execute the command.

import serial

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)


# requests LED ON
def LED_ON():
    ser.write(b'on')


# requests LED OFF
def LED_OFF():
    ser.write(b'off')


# requests LED BLINK
def LED_BLINK():
    ser.write(b'blink')


# requests STATUS
def LED_STATUS():
    ser.write(b'status')
    value = ser.readline()
    valueString = str(value, 'UTF-8')
    print("LED: " + valueString.strip())


# asks for input/command in the terminal
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
    elif command == "stop":
        break
    else:
        print("unknown command")
        print("use: on, off, blink, status or stop")
