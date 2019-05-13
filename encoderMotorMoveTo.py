from robot.megapi import *

def onRead(level):
    print("Encoder motor speed Value:%f" %level)
    
def onReadf():
    print("Encoder motor speed")
    
def onForwardFinish(slot):
    sleep(0.4)
    bot.encoderMotorMoveTo(slot,100,-1000,onBackwardFinish)

def onBackwardFinish(slot):
    sleep(0.4)
    bot.encoderMotorMoveTo(slot,100,1000,onForwardFinish)

if __name__ == '__main__': 
    bot = MegaPi()
    
    bot.start("/dev/ttyUSB0")
    bot.encoderMotorRun(1,0)
    bot.encoderMotorSetCurPosZero(1)
    sleep(1)
    onForwardFinish(1)
    #onBackwardFinish(1)
    
    while 1:
        bot.encoderMotorPosition(1,onRead)
        continue