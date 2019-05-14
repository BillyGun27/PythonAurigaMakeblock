from robot.megapi import *

def onForwardFinish(slot):
    sleep(0.4)
    bot.encoderMotorMove(slot,100,-1000,onBackwardFinish)

def onBackwardFinish(slot):
    sleep(0.4);
    print("slot")
    bot.encoderMotorMove(slot,100,1000,onForwardFinish)

if __name__ == '__main__':
    bot = MegaPi()
    
    bot.start("/dev/ttyUSB0")
    #bot.start("/dev/rfcomm0")
    
    bot.encoderMotorRun(1,0)
    sleep(1)
    onForwardFinish(1)
    while 1:
        continue
