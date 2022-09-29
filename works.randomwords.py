#!/usr/bin/python3

import sys
import os
from random import SystemRandom
from time import sleep, localtime, strftime
from pifacecad import PiFaceCAD, SwitchEventListener, IODIR_FALLING_EDGE

# Get SystemRandom (used urandom)
sr = SystemRandom()

#os.execl("/sbin/shutdown","-h","now")

def print_countdown(s):
    while s > 0:
        cad.lcd.home()
        cad.lcd.write("Ask your ? (%is)  " % s)
        sleep(1)
        s -= 1
    
    

cad = PiFaceCAD()
cad.lcd.home()
cad.lcd.backlight_on()
date_string = strftime("%Y/%m/%d")
time_string = strftime("%H:%M:%S")
cad.lcd.write("%s" % date_string)
cad.lcd.write("\n%s" % time_string)

# Get word list
words = []
with open("/etc/dictionaries-common/words",'r') as f:
    for line in f:
        words.append(line.strip())


cad.lcd.clear()
while True:
    if cad.switches[0].value == 1:
        with open("/dev/hwrng", 'rb') as f:
            print_countdown(10)
            cad.lcd.home()
            cad.lcd.write("Clearing HWRNG  ")
            rand = f.read(1048576)
            num_in_bytes = f.read(4)
            realnum = int.from_bytes(num_in_bytes, byteorder=sys.byteorder, signed=False)
            rint = realnum % len(words)
            cad.lcd.home()
            cad.lcd.write("Your word is:  \n")
            cad.lcd.write(words[rint] + "                ")
