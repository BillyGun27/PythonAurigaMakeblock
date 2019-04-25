from robot.meauriga import *
#from robotMegapi.megapi import *
#import robot.movement as move


if __name__ == '__main__':
	bot = MeAuriga()
	#bot = MegaPi()
	
	bot.start("/dev/ttyUSB0")
	#bot.start("/dev/rfcomm0")
	while (1):
		bot.doMove(100, 100)
		print("run forward")
		sleep(2)
		bot.doMove(-100, -100)
		print("run backward")
		sleep(2)
		bot.doMove(0, 0)
		print("stop")
		sleep(2)