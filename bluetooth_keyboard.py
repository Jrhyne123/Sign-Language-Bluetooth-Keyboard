import asyncio
from bleak import BleakScanner, BleakClient
import pydirectinput

TARGET_ADDRESS = "85:89:CC:07:A0:11"

CHARACTERISTIC1_UUID = "FFF1"
CHARACTERISTIC2_UUID = "FFF2"

async def main():
    print("Scanning for Arduino...")

    devices = await BleakScanner.discover(timeout=10.0)

    target = None
    for d in devices:
        print(f"Found: {d.name} | {d.address}")

        if d.address.upper() == TARGET_ADDRESS.upper():
            target = d

    if target is None:
        print("Target address was not found during scan.")
        return

    print(f"Connecting to {target.address}...")

    async with BleakClient(target, timeout=20.0) as client:
        print("Connected:", client.is_connected)

        print("Services:")
        for service in client.services:
            print(service)

        while True:
            available = await client.read_gatt_char(CHARACTERISTIC2_UUID)

            if len(available) > 0 and available[0] == 1:
                value = await client.read_gatt_char(CHARACTERISTIC1_UUID)

                prediction = value.decode().strip().lower()
                if prediction in ['a', 'b']:
                    pydirectinput.press(prediction)

                await client.write_gatt_char(
                    CHARACTERISTIC2_UUID,
                    bytes([0x00]),
                    response=True
                )

            await asyncio.sleep(0.25)

asyncio.run(main())