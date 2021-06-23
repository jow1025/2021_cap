from time import sleep
import pigpio

servoX=pigpio.pi()
servoY=pigpio.pi()
x=15
y=18

def move_up():
    valY=servoY.get_servo_pulsewidth(y)
    if valY+300<=2400:
        valY+=300
        servoY.set_servo_pulsewidth(y,valY)

def move_down():
    valY=servoY.get_servo_pulsewidth(y)
    if valY-300>=600:
        valY-=300
        servoY.set_servo_pulsewidth(y,valY)
    
def move_left():
    valX=servoX.get_servo_pulsewidth(x)
    if valX+300<=2400:
        valX+=300
        servoX.set_servo_pulsewidth(x,valX)
    
def move_right():
    valX=servoX.get_servo_pulsewidth(x)
    if valX-300>=600:
        valX-=300
        servoX.set_servo_pulsewidth(x,valX)
    
def servoReset():
    servoX.set_servo_pulsewidth(x,1500)
    servoY.set_servo_pulsewidth(y,1500)

    