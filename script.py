import func
import RPi.GPIO as GPIO
import time

sensor = 16

try: 
    while True:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(sensor,GPIO.IN)
        if GPIO.input(sensor):
            func.func()
            time.sleep(0.4)
        GPIO.cleanup()
except KeyboardInterrupt:
    pass