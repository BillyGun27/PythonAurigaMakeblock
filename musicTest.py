from multiprocessing import freeze_support

from robot.meauriga import *
#from robotMegapi.megapi import *

if __name__ == '__main__':
    freeze_support()
    bot = MeAuriga()
    #bot = MegaPi()
    #bot.start("/dev/ttyUSB0")
    bot.start("/dev/rfcomm0")
    # bot.startWithHID()
    while True:
        sleep(1);
        print("s")
        bot.digitalWrite(45,1);
        sleep(1)
        bot.pwmWrite(45, 200)
        sleep(1);
        print("d")
        bot.digitalWrite(45,0);
        #sleep(3);
        #print("ss")
        #bot.digitalWrite(45,1);
        #sleep(3);
        #print("dd")
        #bot.digitalWrite(45,0);
        
