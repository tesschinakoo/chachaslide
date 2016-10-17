from Myro import *
init("sim")

#song: cha cha slide (0:30-1:30)

#DEFINING DANCE FUNCTIONS

def totheLeft(): #dance for guy says "to the left"
    turnLeft(1,.5)
    
def totheRight():
    turnRight(1,.5)
    
def takeitback():
    backward(1,.5)

def onehop():
    forward(1,.25)
    backward(1,.25)
    wait(.5)
    
def rightfoot():
    turnLeft(1,.75)
    turnRight(1,.25)

def leftfoot():
    turnRight(1,.75)
    turnLeft(1,.25)

def crisscross():
    turnLeft(2,.5)
    turnRight(4,.5)
    turnLeft(2,.5)
    
def chacha():
    move(1,1)
    wait(4)
    stop()
    
def rightfoottwostomps():
    turnLeft(.5,.25)
    turnRight(.5,.25)
    turnLeft(.5,.25)
    turnRight(.5,.25)
    
def leftfoottwostomps():
    turnRight(.5,.25)
    turnLeft(.5,.25)
    turnRight(.5,.25)
    turnLeft(.5,.25)
    
def slidetotheleft():
    move(1,1)
    wait(1)
    stop()

def slidetotheright():
    move(1,-1)
    wait(1)
    stop()

#FIRSTVERSE
totheLeft()
wait(1)
takeitback()
wait(1.25)
onehop()
wait(1)
rightfoot()
wait(1)
leftfoot()
wait(1)
chacha()

wait(2)

#SECONDVERSE
totheLeft()
wait(1)
takeitback()
wait(1.5)
onehop()
rightfoot()
wait(1)
leftfoot()
wait(1)
chacha()
wait(1)

wait(1)

#NOW ITS TIME TO GET FUNKY
totheRight()
wait(1.5)
totheLeft()
wait(1)
takeitback()
wait(1)
for x in range(0,2):
    onehop()
    wait(.75)

rightfoottwostomps()
wait(1)
leftfoottwostomps()
wait(1)
slidetotheleft()
wait(1)
slidetotheright()
wait(1)
crisscross()
wait(.5)
crisscross()
wait(.5)
chacha()
