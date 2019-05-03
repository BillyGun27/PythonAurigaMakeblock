from robot.megapi import *



if __name__ == '__main__':
    bot = MegaPi()
    
    bot.start("/dev/ttyUSB0")
    #bot.start("/dev/rfcomm0")
    while (1):
        bot.motorMove(100, 100)
        print("run forward")
        sleep(2)
        bot.motorMove(-100, -100)
        print("run backward")
        sleep(2)
        bot.motorMove(0, 0)
        print("stop")
        sleep(2)