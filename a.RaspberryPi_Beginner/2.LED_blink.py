import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
led=11
GPIO.setup(led,GPIO.OUT)
while(1):
        GPIO.output(led,1)
        time.sleep(0.5)
        GPIO.output(led,0)
        time.sleep(0.5)
GPIO.cleanup()

