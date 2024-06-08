#   Students: Ryoma Nonaka & Jonas Skolnik
#   UvAnetID: 14932431 & 14932423
#   Studie: BSc Informatica
#   File: lab1_accel.py
#   Goal: function to read the given accelaration data from the arduino.

import serial

ser = serial.Serial(port='/dev/ttyACM6', baudrate=9600)


# decodes the given data
# The given format is x, y, z
# it returns the variables as a tuple
def get_accelarator():
    ser.flushInput()
    value = ser.readline().decode('UTF-8').strip()
    x, y, z = map(float, value.split(', '))
    return x, y, z
