#from robot.meauriga import *
from robotMegapi.megapi import *

if __name__ == '__main__':
	#bot = MeAuriga()
	bot = MegaPi()

	bot.start()
	bot.encoderMotorRun(4,0)
	sleep(1)
	while 1:
		bot.encoderMotorRun(4,-200)
		sleep(5)
		bot.encoderMotorRun(4,0)
		sleep(5)