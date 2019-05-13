from robot.megapi import *

right = 1
left = 2

deltaTickRight = 0

def onReadAll(level):
    turn = 0
    #turn = 0
    #print(turn)
    #turn+=1
    #print(turn)
    #right = []
    #left = []
    #if turn == 0 :
    #print("Encoder1 motor speed Value:%f" %level)
    #    turn = 1
    #else :
    #    print("Encoder2 motor speed Value:%f" %level)
    #    turn = 0
    
    #if( int(level) > 500):
    #    print("ffffff")
    #deltaTickRight = level
    
def onRead1(level):
    print("Encoder1 motor speed Value:%f" %level)
    #if( int(level) > 500):
    #    print("ffffff")
    #deltaTickRight = level
        
def onRead2(level):
    print("Encoder2 motor speed Value:%f" %level)
    #deltaTickRight = int(level)
    #if( int(level) > 500):
    #    print("ffffff")
    #    print(deltaTickRight)
    
def check(f):
    print(f)

def cmtotick(target):
    #fulltick 360
    #r 3.25
    tick = ( target*360 ) // ( 2*3.14*3.25 )
    return int(tick)


def onForwardFinish(target):
    sleep(0.4)
    tick = cmtotick(target)
    print(tick)
    #bot.encoderMotorMove(right,100, tick * -1,check)
    bot.encoderMotorMove(left,100, tick ,check )
    print(tick)

def onRightFinish():
    sleep(0.4)
    bot.encoderMotorMove(right,100, 0 * -1,check)
    bot.encoderMotorMove(left,100, 495 ,check )
    
def onLeftFinish():
    sleep(0.4)
    bot.encoderMotorMove(right,100, 495 * -1,check)
    bot.encoderMotorMove(left,100, 0 ,check )
    
def onBackwardFinish():
    sleep(0.4)
    tick = cmtotick(target)
    bot.encoderMotorMove(right ,100, tick,check)
    bot.encoderMotorMove(left,100, tick * -1,check )
    print(tick)

if __name__ == '__main__':
    #bot = MeAuriga()
    bot = MegaPi()
    
    bot.start("/dev/ttyUSB0")
    #bot.start("/dev/rfcomm0")
    
    #bot.encoderMotorSetCurPosZero(1)
    #bot.encoderMotorSetCurPosZero(2)
    
    #bot.encoderMotorPosition(right,onRead1)
    #bot.encoderMotorPosition(left,onRead1)
        
    #bot.encoderMotorRun(right ,0)#right
    #bot.encoderMotorRun(left ,0)#left
    
    sleep(1)
    onForwardFinish(20)
    #sleep(3)
    #onForwardFinish(20)
    
    #onRightFinish()
    #sleep(0.5)
    #onBackwardFinish()
    
    #print("d")
    #print(bot.getBuffer())
    s=0
    while s<320:
        bot.encoderMotorPosition(right,onReadAll)
        bot.encoderMotorPosition(left,onReadAll)
        print(bot.getKeeper())
        encoderkey = bot.getKeeper()
        #print(encoderkey.keys())
        if( len(encoderkey.keys()) ):
            print("right")
            print(encoderkey[ bot.getextId(right) ])
            print("left")
            print(encoderkey[ bot.getextId(left) ])
            
            s=encoderkey[ bot.getextId(left) ]
        sleep(0.1)
        
        continue


