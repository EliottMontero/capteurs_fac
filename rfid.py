import os, sys
from serial import Serial
import time

# ser = serial.Serial('/dev/ttyUSB0',19200, timeout = 5)
#
# # listen for the input, exit if nothing received in timeout period

# while True:
#
#    line = ser.readline()
#    if len(line) == 0:
#       print("Timi.decode('utf-8')e out! Exit.\n")
#       sys.exit()
#    print(line)


ser = Serial('/dev/ttyUSB0',19200, timeout = 20)

while True:
    print("Ecrivez votre commande pour le lecteur rfid")
    cmd = input()
    if cmd == 'fa':
        print("mode lecture")
        msg = ser.readline()
        rfidtag = ''
        for i in msg:
            rfidtag = rfidtag + hex(i).decode('hex')
        print(rfidtag)
    cmd = bytes.fromhex(cmd)
    ser.write(cmd)


# ser.write(bytes.fromhex('fe'))
