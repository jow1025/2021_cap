from gpiozero import Servo
from gpiozero.tools import sin_values
from time import sleep

servoX = Servo(15)
servoY = Servo(18)

# def init():
#     global isInit, valX, valY
#     isInit=True
#     valX=0
#     valY=0

def move_up():
    servoY.value+=0.3

def move_down():
    servoY.value-=0.3
    
def move_left():
    servoX.value-=0.3
    
def move_right():
    servoX.value+=0.3
    
def servoReset():
    servoX.value=0
    servoY.value=0

def printServo():
    print(servoX.value)
    print(servoY.value)

while True:
    servoReset()
    printServo()
    sleep(2)
    
    move_left()
    printServo()
    sleep(0.5)
    move_left()
    printServo()
    sleep(0.5)
    move_left()
    printServo()
    sleep(0.5)
    
    move_up()
    printServo()
    sleep(0.5)
    move_up()
    printServo()
    sleep(0.5)
    move_up()
    printServo()
    sleep(0.5)
    
    move_right()
    printServo()
    sleep(0.5)
    move_right()
    printServo()
    sleep(0.5)
    move_right()
    printServo()
    sleep(0.5)
    move_right()
    printServo()
    sleep(0.5)
    move_right()
    printServo()
    sleep(0.5)
    move_right()
    printServo()
    sleep(0.5)
    
    move_down()
    printServo()
    sleep(0.5)
    move_down()
    printServo()
    sleep(0.5)
    move_down()
    printServo()
    sleep(0.5)
    move_down()
    printServo()
    sleep(0.5)
    move_down()
    printServo()
    sleep(0.5)
    move_down()
    printServo()
    sleep(0.5)

