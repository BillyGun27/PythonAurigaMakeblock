from robot.meauriga import *

def MoveForward(bot):
    bot.motorMove(100,100)

def MoveBackward(bot):
    bot.motorMove(-100,-100)

def MoveLeft(bot):
    bot.motorMove(100,0)

def MoveRight(bot):
    bot.motorMove(0,100)