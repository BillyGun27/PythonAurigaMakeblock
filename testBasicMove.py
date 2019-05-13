from robot.megapi import *

right = 1
left = 2

deltaTickRight = 0

def onRead1(level):
    print("Encoder1 motor speed Value:%f" %level)
    #if( int(level) > 500):
    #    print("ffffff")
    #deltaTickRight = level
        
def onRead2(level):
    print("Encoder2 motor speed Value:%f" %level)
    #deltaTickRight = int(level)
    #if( int(level) > 500):
    #    print("ffffff")
    #    print(deltaTickRight)
    
def check(f):
    print(f)

def onForwardFinish():
    sleep(0.4)
    bot.encoderMotorMove(right,100, 720 * -1,check)
    bot.encoderMotorMove(left,100, 720 ,check )

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
    bot.encoderMotorMove(right ,100, 720,check)
    bot.encoderMotorMove(left,100, -720,check )

if __name__ == '__main__':
    #bot = MeAuriga()
    bot = MegaPi()
    
    #bot.start("/dev/ttyUSB0")
    bot.start("/dev/rfcomm0")
    
    #bot.encoderMotorSetCurPosZero(1)
    #bot.encoderMotorSetCurPosZero(2)
    
    #bot.encoderMotorRun(right ,0)#right
    #bot.encoderMotorRun(left ,0)#left
    
    sleep(0.5)
    print("forward")
    onForwardFinish()
    print("end forward")
    sleep(0.5)
    #onRightFinish()
    #sleep(0.5)
    #onBackwardFinish()
    
    #sleep(2)
    #bot.encoderMotorPosition(1,onRead1)
    #sleep(1)
    #bot.encoderMotorPosition(2,onRead2)
    #while 1:
        #if( deltaTickRight  >  ( 720 - 10 ) ):
        #    print("next order")
        #else :
            #bot.encoderMotorPosition(1,onRead1)
    #    bot.encoderMotorPosition(2,onRead2)
        #print(deltaTickRight)
        #print( bot.getDict() )
    #    sleep(1)
    #    continue

