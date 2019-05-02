#!/usr/bin/python3

# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py

#from lib.mBot import *
from robotMegapi.megapi import *
import sys, termios, tty, os, time

#bot = mBot()
#bot.startWithSerial("/dev/rfcomm0")

bot = MegaPi()

#bot.start("/dev/ttyUSB0")
bot.start("/dev/rfcomm0")

def onRead1(level):
    print("Encoder1 motor speed Value:%f" %level)
    
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

char = ""
time_move = 0.04
speed = 200
def stop_():
    char = "x"

while True:
    char = getch()

    if (char == "q"):
        print("\nis quite !")
        sys.exit()

    if (char == "a"):
        print("\left !")
        bot.motorMove(1*speed, -1*speed)

    elif (char == "d"):
        bot.motorMove(-1*speed, 1*speed)

    elif (char == "w"):
        bot.motorMove(1*speed, 1*speed)

    elif (char == "s"):
        bot.motorMove(-1*speed, -1*speed)

    elif (char == "x"):
        bot.motorMove(0, 0)

    sleep(time_move)
    bot.encoderMotorPosition(1,onRead1)
    bot.motorMove(0, 0)