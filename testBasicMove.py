#from robot.meauriga import *
from robotMegapi.megapi import *

right = 1
left = 2

def onRead1(level):
    print("Encoder1 motor speed Value:%f" %level)
        
def onRead2(level):
    print("Encoder2 motor speed Value:%f" %level)
    
def check(f):
    print(f)

def onForwardFinish():
    sleep(0.4)
    bot.encoderMotorMove(right,100, 1000 * -1,check)
    bot.encoderMotorMove(left,100, 1000 ,check )

def onRightFinish():
    sleep(0.4)
    bot.encoderMotorMove(right,100, 0 * -1,check)
    bot.encoderMotorMove(left,100, 495 ,check )
    
def onLeftFinish():
    sleep(0.4)
    bot.encoderMotorMove(right,100, 495 * -1,check)
    bot.encoderMotorMove(left,100, 0 ,check )
    
def onBackwardFinish():
    sleep(0.4)
    print("slot")
    bot.encoderMotorMove(right ,100, 360,check)
    bot.encoderMotorMove(left,100, -360,check )

if __name__ == '__main__':
    #bot = MeAuriga()
    bot = MegaPi()
    
    #bot.start("/dev/ttyUSB0")
    bot.start("/dev/rfcomm0")
    
    bot.encoderMotorSetCurPosZero(1)
    bot.encoderMotorSetCurPosZero(2)
    
    bot.encoderMotorRun(right ,0)#right
    bot.encoderMotorRun(left ,0)#left
    
    sleep(1)
    onForwardFinish()
    sleep(1)
    onRightFinish()
    #onBackwardFinish()
    
    #while 1:
    #    bot.encoderMotorPosition(1,onRead1)
    #    bot.encoderMotorPosition(2,onRead2)
    #    continue

