def barricade():
    import RPi.GPIO as GPIO
    from time import sleep
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40, GPIO.OUT)
    pwm=GPIO.PWM(40, 50)
    pwm.start(0)
    def SetAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(40, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(40, False)
        pwm.ChangeDutyCycle(0)
    SetAngle(120)
    sleep(10)
    SetAngle(30)
    pwm.stop()
    GPIO.cleanup()