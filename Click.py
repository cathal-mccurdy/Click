import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)

kill = input('Press E to End')

while True:
    if GPIO.input(7) == 1:
        print('Ouch!')
    else:
        print('Push me!')

    GPIO.cleanup()

    if kill = 'e':
        sys.exit(0)
    else:
    #this kills the program

    
