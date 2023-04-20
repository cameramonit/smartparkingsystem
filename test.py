def button():
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23

    try:
        while True:
            button_state = GPIO.input(23)
            if button_state == False:
                print('Button Pressed...')
    except:
        GPIO.cleanup()

def checkspace():
    import scan
    import checkspace

    scan.scan()
    
    empty_image = 'images/test.jpg'
    current_image = 'images/target.jpg'

    coordinates = [30, 378, 236, 381, 250, 287, 63, 284]

    empty = checkspace.avg_dark_pixels(empty_image, coordinates)
    current = checkspace.avg_dark_pixels(current_image, coordinates)

    if abs(current - empty) < 30:
        print("empty:", empty)
        print("current:", current)
        print("Parking space empty")
    else:
        print("empty:", empty)
        print("current:", current)
        print("Parking space occupied")

def checkall():

    import scan
    import checkspace

    scan.scan()
    
    empty_image = 'images/test.jpg'
    current_image = 'images/target.jpg'

    coordinates = [[231, 437, 36, 453, 60, 363, 235, 346],
[238, 302, 66, 320, 84, 248, 239, 232],
[243, 203, 93, 216, 107, 145, 244, 125],
[625, 389, 423, 411, 412, 324, 585, 303],
[576, 266, 409, 287, 398, 216, 555, 199],
[547, 172, 392, 186, 388, 114, 523, 102]]

    coordinates_flag = [0,0,0,0,0,0]
    available = []

    for index, item in enumerate(coordinates):

        empty = checkspace.avg_dark_pixels(empty_image, item)
        current = checkspace.avg_dark_pixels(current_image, item)

        if abs(current - empty) < 10:
            coordinates_flag[index] = 0     # if empty
            available.append(index+1)
        else:
            coordinates_flag[index] = 1     # if occupied

    import random

    print(coordinates_flag)
    print(available)

def showall():

    import scan
    import checkspace

    scan.scan()
    
    empty_image = 'images/test.jpg'
    current_image = 'images/target.jpg'

    coordinates = [[231, 437, 36, 453, 60, 363, 235, 346],
[238, 302, 66, 320, 84, 248, 239, 232],
[243, 203, 93, 216, 107, 145, 244, 125],
[625, 389, 423, 411, 412, 324, 585, 303],
[576, 266, 409, 287, 398, 216, 555, 199],
[547, 172, 392, 186, 388, 114, 523, 102]]

    coordinates_flag = [0,0,0,0,0,0]
    available = []

    for index, item in enumerate(coordinates):

        empty = checkspace.avg_dark_pixels(empty_image, item)
        current = checkspace.avg_dark_pixels(current_image, item)

        if abs(current - empty) < 10:
            coordinates_flag[index] = 0     # if empty
            available.append(index+1)
        else:
            coordinates_flag[index] = 1     # if occupied

        print()
        print("Slot: ", index+1)
        print("Empty: ", empty)
        print("Current: ", current)
        print()

    import random

    if(len(available)>0):
        print("Park at slot: ", random.choice(available))
    else:
        print("No space.")

def print():    # using standard LCD wiring
    from RPLCD import CharLCD
    from RPi import GPIO

    # Define the GPIO pins connected to the LCD
    lcd_rs = 25
    lcd_en = 24
    lcd_d4 = 23
    lcd_d5 = 17
    lcd_d6 = 18
    lcd_d7 = 22
    lcd_backlight = 2

    # Define the number of columns and rows of the LCD
    lcd_columns = 16
    lcd_rows = 2

    # Initialize the LCD object
    lcd = CharLCD(
        cols=lcd_columns,
        rows=lcd_rows,
        pin_rs=lcd_rs,
        pin_e=lcd_en,
        pins_data=[lcd_d4, lcd_d5, lcd_d6, lcd_d7],
        numbering_mode=GPIO.BCM
    )

    # Print a message on the LCD
    lcd.write_string('Hello, world!')

def i2c():
    from signal import signal, SIGTERM, SIGHUP, pause
    from rpi_lcd import LCD
    lcd = LCD()
    def safe_exit(signum, frame):
        exit(1)
    try:
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
        lcd.text("Hello,", 1)
        lcd.text("Raspberry Pi!", 2)
        pause()
    except KeyboardInterrupt:
        pass
    finally:
        lcd.clear()

def servo():
    import RPi.GPIO as GPIO
    from time import sleep
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    pwm=GPIO.PWM(3, 50)
    pwm.start(0)
    def SetAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(3, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(3, False)
        pwm.ChangeDutyCycle(0)
    SetAngle(120)
    sleep(5)
    SetAngle(30)
    pwm.stop()
    GPIO.cleanup()

def ir():
    import RPi.GPIO as GPIO
    import time
    import print

    sensor = 16

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor,GPIO.IN)

    try: 
        while True:
            if GPIO.input(sensor):
                print("Object Detected")
                while GPIO.input(sensor):
                    time.sleep(0.4)
    except KeyboardInterrupt:
        GPIO.cleanup()