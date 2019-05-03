from robotMegapi.megapi import *

def onRead(level):
    print("Encoder motor speed Value:%f" %level)

if __name__ == '__main__':
    bot = MegaPi()
    
    bot.start("/dev/ttyUSB0")
    
    bot.encoderMotorRun(1,0)
    sleep(1)
    #bot.encoderMotorRun(1,100)
    #sleep(2)
    while 1:
        bot.encoderMotorPosition(1,onRead)
        sleep(0.2)