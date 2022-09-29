#!/usr/bin/python3

import sys
import os
from time import sleep, localtime, strftime
from pifacecad import PiFaceCAD, SwitchEventListener, IODIR_FALLING_EDGE, LCDBitmap


def print_countdown(s):
    while s > 0:
        cad.lcd.home()
        cad.lcd.write("Ask your ? (%is)  " % s)
        sleep(1)
        s -= 1
    
def print_randword():
    with open("/dev/hwrng", 'rb') as f:
        print_countdown(5)
        cad.lcd.home()
        cad.lcd.write("Clearing HWRNG  ")
        rand = f.read(1048576)
        num_in_bytes = f.read(4)
        realnum = int.from_bytes(num_in_bytes, byteorder=sys.byteorder, signed=False)
        rint = realnum % len(words)
        cad.lcd.home()
        cad.lcd.write("Your word is:  \n")
        # Overwrites if old buffer is longer
        cad.lcd.write(words[rint] + "                ")
    
def do_pacman():
    cad.lcd.blink_off()
    cad.lcd.cursor_off()
    pacman = LCDBitmap([0x0,0xe,0x11,0x12,0x14,0x12,0x11,0xe])
    ghost = LCDBitmap([0x0,0xe,0x1f,0x15,0x1f,0x1f,0x1f,0x15])
    ghost_eyes = LCDBitmap([0x0,0x0,0x0,0xa,0x0,0x0,0x0,0x0])
    cad.lcd.clear()
    cad.lcd.store_custom_bitmap(0, pacman)
    cad.lcd.store_custom_bitmap(1, ghost)
    cad.lcd.store_custom_bitmap(2, ghost_eyes)
    cad.lcd.write_custom_bitmap(0)
    cad.lcd.write(" ")
    cad.lcd.write_custom_bitmap(1)
    cad.lcd.write_custom_bitmap(1)
    cad.lcd.write_custom_bitmap(1)
    cad.lcd.write("\n")
    for x in range(16):
        cad.lcd.move_right()
        sleep(.30)
    cad.lcd.clear()
    for x in range(16):
        cad.lcd.move_right()
    cad.lcd.write_custom_bitmap(2)
    cad.lcd.write_custom_bitmap(2)
    cad.lcd.write_custom_bitmap(2)
    sleep(2)
    for x in range(16):
        cad.lcd.move_left()
        sleep(.30)
    sleep(1)
    cad.lcd.clear()


# Init display
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

while (cad.switches[0].value == 0 and 
       cad.switches[2].value == 0):
    # Tight loop, clears when past
    pass

cad.lcd.clear()
cont_run = False # default mode


while True:
    # Get switch state instance
    inst_switches = []
    for x in range(5):
        inst_switches.append(cad.switches[x].value)
    if inst_switches[0] == 1 and cont_run:
        cad.lcd.home()
        cad.lcd.write("Switching mode:\n")
        cad.lcd.write("Press to play")
        sleep(3)
        cad.lcd.clear()
        cont_run = False
    elif inst_switches[0] == 1 or cont_run:
        print_randword()
    elif inst_switches[1] == 1:
        cad.lcd.home()
        cad.lcd.write("Switching mode:\n")
        cad.lcd.write("Continuous play")
        sleep(1)
        cad.lcd.clear()
        cont_run = True
    elif inst_switches[2] == 1:
        do_pacman()
    elif inst_switches[4] == 1:
        cad.lcd.clear()
        cad.lcd.write("Shutting down!\n") 
        cad.lcd.write("Wait 15s, unplug") 
        os.execl("/sbin/shutdown","-h","now")
