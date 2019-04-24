from robot.meauriga import *
#from robotMegapi import *

def onRead(v):
	print("sound:"+str(v))

if __name__ == '__main__':
	bot = MeAuriga()
	#bot = MegaPi()

	bot.start("/dev/ttyUSB0")
	#bot.start("/dev/rfcomm0")
	while 1:
		sleep(0.1)
		bot.soundSensorRead(14,onRead)
