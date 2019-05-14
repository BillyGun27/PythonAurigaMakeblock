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

    commandDir=["forward","forward","backward"]
    commandDist=[[40,40,40] #cm

    #bot.encoderMotorSetCurPosZero(right)
    #bot.encoderMotorSetCurPosZero(left)
    
    #bot.encoderMotorRun(right ,0)#right
    #bot.encoderMotorRun(left ,0)#left
    
    sleep(0.5)
   
    i = 0
    #targetTickRight = cmtotick(commandDist)
    targetTick = cmtotick(commandDist[i])
    onExecuteDir(commandDir[i],targetTick)
    
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
           
            deltaTickRight = encRight - lastTickRight
            deltaTickLeft = encLeft - lastTickLeft
            print("Right: Delta>{} Cur>{} Last>{}".format( deltaTickRight, encRight ,lastTickRight ))
            print("Left: Delta>{} Cur>{} Last>{}".format( deltaTickLeft, encLeft ,lastTickLeft ))
            print("Target:{}".format(targetTick) )
            #Position Reached
            if  ( abs(deltaTickRight)-20 ) < abs(targetTick) < ( abs(deltaTickRight)+20 ) 
            and ( abs(deltaTickLeft)-20 ) < abs(targetTick) < ( abs(deltaTickLeft)+20 )    :
                 if not command:
                    print("change")
                    if i<len(commandDir):
                        i+=1
                    else:
                        break 
                    targetTick = cmtotick(commandDist[i])
                    onExecuteDir(commandDir[i],targetTick)
                    command = True
            elif command :
                command = False
            
        sleep(0.1)
        
        continue


