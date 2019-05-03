from robotMegapi.megapi import *

if __name__ == '__main__':
    bot = MegaPi()

    bot.start("/dev/ttyUSB0")
     
    bot.encoderMotorRun(1,0)
    sleep(1)
    while 1:
        bot.encoderMotorRun(1,-200)
        sleep(5)
        bot.encoderMotorRun(1,0)
        sleep(5)