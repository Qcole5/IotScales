import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def readNumber():
   number = bus.read_i2c_block_data(address)
   # number = bus.read_byte_data(address, 1)
   return number

while True:
   number = readNumber()
   print( "MSP432: Hey RPI, I received a ", number)
