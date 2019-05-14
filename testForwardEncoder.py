from robot.megapi import *

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
    
    bot.encoderMotorMove(right,100, 500 * -1,check)
    bot.encoderMotorMove(left,100, 500 ,check )
    
    print("no slot")
    
    #bot.encoderMotorPosition(1,onRead1)#right
    #bot.encoderMotorPosition(2,onRead2)#left

def onBackwardFinish():
    sleep(0.4)
    print("slot")
    bot.encoderMotorMove(right ,100, 500,check)
    bot.encoderMotorMove(left,100, 500 * -1,check )

if __name__ == '__main__':
    #bot = MeAuriga()
    bot = MegaPi()
    
    bot.start("/dev/ttyUSB0")
    #bot.start("/dev/rfcomm0")
    
    bot.encoderMotorSetCurPosZero(1)
    bot.encoderMotorSetCurPosZero(2)
    
    #bot.encoderMotorRun(right ,0)#right
    #bot.encoderMotorRun(left ,0)#left
    
    sleep(1)
    onForwardFinish()
    
    
    while 1:
        bot.encoderMotorPosition(right,onRead1)
        bot.encoderMotorPosition(left,onRead2)
        sleep(0.5)
        continue
