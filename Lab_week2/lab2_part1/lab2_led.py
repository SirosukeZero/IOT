#LAB2_led_template.py template for lab2 part 1
#Taco Walstra, may 2024
import argparse
import asyncio
import struct

from bleak import BleakClient
from bleak import BleakScanner
from bleak import discover

ARDUINO_LOCAL_NAME = "BLE-LAB41"  #Use the correct Arduino number in this identifier!!

LED_UUID = "19B10000-E8F2-537E-4F6C-D104768A1214"
CHARACTERISTIC_UUID = "19B10001-E8F2-537E-4F6C-D104768A1214"

on_value = bytearray([0x01])
off_value = bytearray([0x00])


async def find_ble_device(args: argparse.Namespace):
    print("scanning for 5 seconds, please wait...")

    devices = await BleakScanner.discover(
        return_adv=True, cb=dict(use_bdaddr=args.macos_use_bdaddr)
    )
    
    # find your Arduino and return device and address
    for d, a in devices.values():
        if a.local_name == ARDUINO_LOCAL_NAME:
            return (d, a)


async def runmain(d, a):
    async with BleakClient(d.address) as client:
        svcs = await client.get_services()
        # Get the characteristic object using its UUID
        characteristic = svcs.get_characteristic(CHARACTERISTIC_UUID)
        await client.write_gatt_char(characteristic, on_value)
        await asyncio.sleep(1)
        await client.write_gatt_char(characteristic, off_value)

       
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
    (d, a) = asyncio.run(find_ble_device(args))
    if (d, a) != (None, None):
        asyncio.run(runmain(d, a))
    else:
        print("arduino not found")
