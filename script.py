import func
import RPi.GPIO as GPIO
import time

sensor = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)

try: 
    while True:
        GPIO.setmode(GPIO.BOARD)
        if GPIO.input(sensor):
            func.func()
            time.sleep(0.4)
        GPIO.cleanup()
except KeyboardInterrupt:
    pass