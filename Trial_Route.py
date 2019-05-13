from robot.megapi import *

right = 1
left = 2

deltaTickRight = 0
def check(t):
    print(t)

def cmtotick(target):
    #fulltick 360
    #r 3.25
    tick = ( target*360 ) // ( 2*3.14*3.25 )
    return int(tick)

def onForwardFinish(tick):
    #bot.encoderMotorMove(right,100, tick * -1,check)
    bot.encoderMotorMove(left,100, tick ,check )
    print(tick)

def onRightFinish():
    bot.encoderMotorMove(right,100, 0 * -1,check)
    bot.encoderMotorMove(left,100, 495 ,check )
    
def onLeftFinish():
    bot.encoderMotorMove(right,100, 495 * -1,check)
    bot.encoderMotorMove(left,100, 0 ,check )
    
def onBackwardFinish(tick):
    bot.encoderMotorMove(right ,100, tick,check)
    #bot.encoderMotorMove(left,100, tick * -1,check )
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
    
    sleep(0.4)
    target = 20 #cm
    tick = cmtotick(target)
    print(tick)

    sleep(1)
    onForwardFinish(tick)
    #sleep(3)
    #onForwardFinish(20)
    
    #onRightFinish()
    #sleep(0.5)
    #onBackwardFinish()
    
    #print("d")
    #print(bot.getBuffer())
    command = False
    while True:
        bot.encoderMotorPos(right)
        bot.encoderMotorPos(left)
        print(bot.getKeeper())
        encoderkey = bot.getKeeper()
        #print(encoderkey.keys())
        if( len(encoderkey.keys()) ):
            encRight =  encoderkey[ bot.getextId(right) ]
            encLeft = encoderkey[ bot.getextId(left) ]

            print("right" + str(encRight))
            print("left" + str(encLeft))
            if encLeft > (tick-20) and not command:
                print("change")
                onBackwardFinish(tick)
                command = True
            
        sleep(0.1)
        
        continue


