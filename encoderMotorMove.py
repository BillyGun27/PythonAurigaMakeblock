from robot.megapi import *

def onRead1(level):
    print("Encoder1 motor speed Value:%f" %level)
        
def onRead2(level):
    print("Encoder2 motor speed Value:%f" %level)
    
def check(f):
    print(f)

def onForwardFinish(slot):
    sleep(0.4)
    print("no slot")
    bot.encoderMotorMove(slot,10,180,check )

def onBackwardFinish(slot):
    sleep(0.4)
    print("slot")
    bot.encoderMotorMove(slot,10,250,check )

if __name__ == '__main__':
    bot = MegaPi()
    
    bot.start("/dev/ttyUSB0")
    #bot.start("/dev/rfcomm0")
    
    bot.encoderMotorRun(1,0)
    bot.encoderMotorRun(2,0)
    sleep(1)
    onForwardFinish(2)
    
    while 1:
        #bot.encoderMotorPosition(1,onRead1)
        bot.encoderMotorPosition(2,onRead2)
        continue