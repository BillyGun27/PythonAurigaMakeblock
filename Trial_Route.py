from robot.megapi import *

right = 1
left = 2

def cmtotick(target):
    #fulltick 360
    #r 3.25
    tick = ( target*360 ) // ( 2*3.14*3.25 )
    return int(tick)

def onForwardFinish(tick):
    bot.encoderMotorMover(right, 100, tick * -1 )
    bot.encoderMotorMover(left, 100, tick )

def onRightFinish():
    bot.encoderMotorMover(right,100, 0 * -1 )
    bot.encoderMotorMover(left, 100, 495 )
    
def onLeftFinish():
    bot.encoderMotorMover(right, 100, 495 * -1 )
    bot.encoderMotorMover(left, 100, 0 )
    
def onBackwardFinish(tick):
    bot.encoderMotorMover(right, 100, tick)
    bot.encoderMotorMover(left, 100, tick * -1 )
    
def onExecuteDir(dir,tick):
    if dir == "forward" :
        onForwardFinish(tick)
    elif dir == "backward" :
        onBackwardFinish(tick)
    elif dir == "right" :
        onForwardFinish(tick)
    elif dir == "left" :
        onBackwardFinish(tick)

def EncoderGroup():
    bot.encoderMotorPos(right)
    bot.encoderMotorPos(left)
    
    return bot.getKeeper()

if __name__ == '__main__':
    bot = MegaPi()
    bot.start("/dev/ttyUSB0")
    #bot.start("/dev/rfcomm0")

    commandDir=["forward","left","forward","backward","right"]
    commandDist=[[40,0,40,40,0]

    #bot.encoderMotorSetCurPosZero(right)
    #bot.encoderMotorSetCurPosZero(left)
    
    #bot.encoderMotorRun(right ,0)#right
    #bot.encoderMotorRun(left ,0)#left
    
    sleep(0.4)
    target = 20 #cm
    tick = cmtotick(target)
    print(tick)

    sleep(1)
    onForwardFinish(tick)
    
    lastTickRight = 0
    lastTickLeft = 0
    command = False
    while True:
        encodergroup =  EncoderGroup()
        #print(encoderkey.keys())
        
        ###wait encoder value
        if( len(encodergroup.keys()) ):
            print(encodergroup)

            encRight =  encoderkey[ bot.getextId(right) ]
            encLeft = encoderkey[ bot.getextId(left) ]

            #print("right" + str(encRight))
            #print("left" + str(encLeft))
            if not command:
                if encLeft-lastTickRight > (tick-20) and encRight   :
                    print("change")
                    onBackwardFinish(tick)
                    command = True
            
        sleep(0.1)
        
        continue


