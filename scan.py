import asyncio
from bleak import BleakScanner

async def scan_devices():
    devices = await BleakScanner.discover()
    print(devices)
    for device in devices:
        print(f"Device: {device.name}, Address: {device.address}")
    print()

while True:
    asyncio.run(scan_devices())
