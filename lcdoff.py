#!/usr/bin/python3

import sys
import os
from time import sleep, localtime, strftime
from pifacecad import PiFaceCAD, SwitchEventListener, IODIR_FALLING_EDGE, LCDBitmap


# Init display
cad = PiFaceCAD()
cad.lcd.home()
cad.lcd.backlight_off()

