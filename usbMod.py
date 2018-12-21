#!/usr/bin/python3
import serial
import time

ser1 = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
ser2 = serial.Serial('/dev/ttyACM0', 9600, timeout=5)

# read from Arduino
input1 = ser1.read()
input2 = ser2.read()

def modData(dataArray):
        tmpArray = []
        for i in dataArray:
                #ii = int(i)
                if i > 47 and i < 59:
                        i -= 48    # normalize to 0-9
                        list.append(tmpArray, i)
                
        length = len(tmpArray)
        final = 0
        for i in tmpArray:
                final += i*10**(length-1)
                length -= 1

        return final

while 1:
        time.sleep(2)
        dataStart = []
        for i in range (0,3):
                input1 = ser1.read()
                list.append(dataStart,input1)
        if len(dataStart) == 0:
                pass
        else:
                answer = modData(dataStart)
                print ("Read input1 back: " + answer)
        
                
        dataStart = []
        for i in range (0,3):
                input1 = ser2.read()
                list.append(dataStart,input1)
        if len(dataStart) == 0:
                pass
        else:
                answer = modData(dataStart)
                print ("Read input1 back: " + answer)


        time.sleep(1)
