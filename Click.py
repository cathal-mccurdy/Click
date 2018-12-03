import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN,GPIO.PUD_UP)
#this sets up the pins

while True:
    if GPIO.input(7) == 1:
        print('Ouch!')
    else:
        print('Push me!')
    #this asks if the button has been pressed



   
    
