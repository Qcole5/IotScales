#!/usr/bin/python3


import serial
import time

ser1 = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
ser2 = serial.Serial('/dev/ttyACM0', 9600, timeout=5)


# read from Arduino

input1 = ser1.read()
input2 = ser2.read()

#print ("Read input " + input.decode("utf-8") + " from Arduino")



while 1:

        # write something back

#        ser.write(b'A')



       # read response back from Arduino

        for i in range (0,3):
                input = ser1.read()
                input_number = ord(input)
                print ("Read input1 back: " + str(input_number))

        for i in range (0,3):
                input = ser2.read()
                input_number = ord(input)
                print ("Read input2 back: " + str(input_number))


        time.sleep(1)
