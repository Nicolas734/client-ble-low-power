import asyncio
from bleak import BleakClient, BleakScanner
from struct import pack

BLE_NAME = "ESP32"
SERVICE_UUID = "19b10000-e8f2-537e-4f6c-d104768a1214"
SENSOR_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1214"
LED_CHARACTERISTIC_UUID = "19b10002-e8f2-537e-4f6c-d104768a1214"

async def read_sensor(client):
    sensor_value = await client.read_gatt_char(SENSOR_CHARACTERISTIC_UUID)
    print('Sensor raw value: ', sensor_value)
    print(f"Sensor value: {int.from_bytes(sensor_value, byteorder='little')}") #usando int.from_bytes
    print(f"Sensor value: {int(sensor_value.decode("ascii"))}") #usando int(sensor_value.decode("ascii"))

async def write_led(client, value):
    value_packed = pack("<B", value)
    print('Raw value send: ', value_packed)
    await client.write_gatt_char(LED_CHARACTERISTIC_UUID, value_packed)
    print(f"Written value {value} to LED characteristic")

async def scan_devices() -> list:
    devices = await BleakScanner.discover()
    return devices


async def main():
    while True:
        devices = await scan_devices()

        if len(devices):
            global esp_device
            esp_device = None
            for device in devices:
                if device.name == BLE_NAME:
                    esp_device = device

            if esp_device is not None:
                print("Trying to connect to device: ", esp_device)
                try:
                    async with BleakClient(esp_device.address) as client:
                            print('Connected to device: ', esp_device)
                            while await client.is_connected():
                                #Leitura do valor do sensor
                                await write_led(client, 0)
                                print()
                                await read_sensor(client)
                                print()
                                #Escrever valor para LED (1 para ligar, 0 para desligar)
                                await write_led(client, 1)
                                print()
                                await asyncio.sleep(3)
                except Exception as e:
                    print("Fail to connect")
                    print(e)
            else:
                print(f"Device {BLE_NAME} não encontrado")
        else:
            print("Nenhum dispositivo encontrado")

asyncio.run(main())
