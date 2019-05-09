from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
btn=12

GPIO.setup(btn,GPIO.IN,pull_up_down=GPIO.PUD_UP)


while(1):
        if GPIO.input(btn)==0:
                print "Button pressed"
                sleep(.1)

GPIO.cleanup()
