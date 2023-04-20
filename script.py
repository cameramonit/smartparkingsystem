import RPi.GPIO as GPIO
import time
import func

sensor = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)

try: 
    while True:
        if GPIO.input(sensor):
            func.func()
            while GPIO.input(sensor):
                time.sleep(0.4)
except KeyboardInterrupt:
    GPIO.cleanup()