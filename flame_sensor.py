import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
FLAME = 16
BUZZER = 18
GAS = 12
GPIO.setup(FLAME,GPIO.IN)
GPIO.setup(GAS,GPIO.IN)
GPIO.setup(BUZZER,GPIO.OUT)
while True:
	#if GPIO.input(FLAME)==1 :
	#	GPIO.output(BUZZER,GPIO.LOW)
	#else:
	#	 GPIO.output(BUZZER,GPIO.HIGH)
	if GPIO.input(GAS)==1 :
		GPIO.output(BUZZER,GPIO.HIGH)
	else: GPIO.output(BUZZER,GPIO.LOW)
		
