import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servo=11
GPIO.setup(servo,GPIO.OUT)
x=GPIO.PWM(servo,50)
x.start(2)
while(1):
        pos=input("angle= ")
        DutyCy=11./180.*(pos)+2
        x.ChangeDutyCycle(DutyCy)
x.stop()
GPIO.cleanup()
