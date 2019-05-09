import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
x=GPIO.PWM(11,100)
x.ChangeFrequency(100)
x.start(0)
while(1):
        for i in range(0,100,1):
                x.ChangeDutyCycle(i)
                time.sleep(.03)
        for j in range(100,0,-1):
                x.ChangeDutyCycle(j)
                time.sleep(0.03)

x.stop()
GPIO.cleanup()
