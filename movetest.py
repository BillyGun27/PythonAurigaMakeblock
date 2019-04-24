from robot.meauriga import *
import robot.movement as move


if __name__ == '__main__':
	bot = MeAuriga()
	#bot.start("/dev/ttyUSB0")
	bot.startWithSerial("/dev/rfcomm0")
	while 1:
		sleep(0.1)
		move.MoveForward(bot)
        sleep(2)
        move.MoveRight(bot)