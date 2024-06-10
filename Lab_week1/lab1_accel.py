#   Students: Ryoma Nonaka & Jonas Skolnik
#   UvAnetID: 14932431 & 14932423
#   Studie: BSc Informatica
#   File: lab1_accel.py
#   Goal: function to read the given accelaration data from the arduino.

import serial

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)


# decodes the given data
# The given format is x, y, z
# it returns the variables as a tuple

# We rounded the 3 accelerometer values to one decimal,
# We did this because it has a sensor accuracy error of ± 0.04
# Which mean that the second decimal isn't trustworthy,
# that's why we round it to only one deicmal

def get_accelarator():
    ser.flushInput()
    value = ser.readline().decode('UTF-8').strip()
    x, y, z = map(float, value.split(', '))
    return round(x, 1), round(y, 1), round(z, 1)
