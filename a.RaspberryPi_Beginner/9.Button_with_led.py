from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

led=11
button=12

GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT)
LED_value=False
while(1):
        if GPIO.input(button)==0:
                print "Button was pressed"
                if LED_value==False:
                        GPIO.output(led,True)
                        LED_value=True
                        sleep(.5)
                else:
                        GPIO.output(led,False)
                        LED_value=False
                        sleep(.5)
GPIO.cleanup()
