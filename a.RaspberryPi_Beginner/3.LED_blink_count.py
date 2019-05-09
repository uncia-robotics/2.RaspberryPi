import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
led=11
GPIO.setup(led,GPIO.OUT)

number = input ("How Many Times? ")
for i in range (0,number):
        GPIO.output(led,1)
        time.sleep(0.5)
        GPIO.output(led,0)
        time.sleep(0.5)
GPIO.cleanup
