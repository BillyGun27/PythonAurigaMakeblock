from robot.meauriga import *
#from robotMegapi import *

def onRead(v):
	print("distance:"+str(v)+" cm")

if __name__ == '__main__':
	bot = MeAuriga()
	#bot = MegaPi()

	bot.start("/dev/ttyUSB0")
	#bot.start("/dev/rfcomm0")
	while 1:
		sleep(0.1)
		bot.ultrasonicSensorRead(10,onRead)
