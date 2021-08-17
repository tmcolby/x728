#!/usr/bin/python3
import struct
import smbus
import sys
import time
import RPi.GPIO as GPIO

# Global settings
# GPIO is 26 for x728 v2.0, GPIO is 13 for X728 v1.2/v1.3
GPIO_PORT   = 26
I2C_ADDR    = 0x36

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PORT, GPIO.OUT)
GPIO.setwarnings(False)

def readVoltage(bus):

     address = I2C_ADDR
     read = bus.read_word_data(address, 2)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     voltage = swapped * 1.25 /1000/16
     return voltage

def readCapacity(bus):

     address = I2C_ADDR
     read = bus.read_word_data(address, 4)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     capacity = swapped/256
     return capacity

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)


while True:
 print("******************")
 print(f"Voltage: {readVoltage(bus):2.2f}V")
 print(f"Battery: {readCapacity(bus):3.1f}%")
 if readCapacity(bus) == 100:
         print("Battery FULL")
 if readCapacity(bus) < 20:
         print("Battery Low")
#Set battery low voltage to shut down, you can modify the 3.00 to other value
 if readVoltage(bus) < 3.1:
         print("Battery LOW!!!")
         print("Shutdown in 10 seconds")
         time.sleep(10)
         GPIO.output(GPIO_PORT, GPIO.HIGH)
         time.sleep(3)
         GPIO.output(GPIO_PORT, GPIO.LOW)
 time.sleep(2)

