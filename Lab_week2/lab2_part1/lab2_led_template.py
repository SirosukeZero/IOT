#LAB2_led_template.py template for lab2 part 1
#Taco Walstra, may 2024
import argparse
import asyncio
import struct

from bleak import BleakClient
from bleak import BleakScanner
from bleak import discover

ARDUINO_LOCAL_NAME = "BLE-AR33"  #Use the correct Arduino number in this identifier!!

LED_UUID = "19b10001-e8f2-537e-4f6c-d104768a1214"

on_value = bytearray([0x01])
off_value = bytearray([0x00])

async def find_ble_device(args: argparse.Namespace):
    print("scanning for 5 seconds, please wait...")

    devices = await BleakScanner.discover(
        return_adv=True, cb=dict(use_bdaddr=args.macos_use_bdaddr)
    )

#
# find your Arduino and return device and address
    return (d,a)


async def runmain(d,a):

    async with BleakClient(d.address) as client:
        await client.connect()
        print("Connected to Arduino")
            
        svcs = await client.get_services()
        print(f"Services: {svcs}")


# your code here to control the led.
# use await statements and the bleak read_gatt_char and write_gatt_char
# functions of Bleak
#flash the LED 10 times with one second in between using an asynchronous sleep



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--macos-use-bdaddr",
        action="store_true",
        help="when true use Bluetooth address instead of UUID on macOS",
    )


    args = parser.parse_args()
    (d,a) = asyncio.run(find_ble_device(args))
    if (d,a) != (None, None):
      asyncio.run(runmain(d,a))
    else:
        print("arduino not found")
