from gpiozero import Servo
from gpiozero.tools import sin_values
from time import sleep

servoX = Servo(15)
servoY = Servo(18)

def move_up():
    servoY.value+=0.3

def move_down():
    servoY.value-=0.3
    
def move_left():
    servoX.value+=0.3
    
def move_right():
    servoX.value-=0.3
    
def servoReset():
    servoX.value=0
    servoY.value=0