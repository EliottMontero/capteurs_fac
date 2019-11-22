import os, sys
from serial import Serial
import time

openTag = ''

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
        if openTag == '':
            openTag = rfidTag
        if openTag == rfidTag:
            print("OUVERT\n")
        else:
            print("MAUVAISE ID\n")
    # cmd = bytes.fromhex(cmd)
    # ser.write(cmd)


# ser.write(bytes.fromhex('fe'))
