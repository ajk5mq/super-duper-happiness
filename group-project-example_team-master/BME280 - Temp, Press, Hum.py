# BME280 access from Raspberry Pi
# Andy Kehr, 9/2018


import bme280  # bme280 is a temperature, pressure, humidity sensor
import smbus2
from time import sleep

port = 1
address = 0x77  # address for Adafruit BME280
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

# Function to iteratively read data from sensor and
# write to a file before sleeping for 60 seconds.

bme_data_read():
    f = open("bme280_data.txt", "a")
    bme280_read = bme280.sample(bus,address)  # take a sample from the bme280
    humidity = bme280_read.humidty
    temperature = bme208_read.temperature
    pressure = bme280_read.pressure
    f.write("Hum: " + humidity + "\n"
            "Temp: " + temperature + "\n"
            "Press: " + pressure + "\n" + )
    f.close()
    sleep(60)


