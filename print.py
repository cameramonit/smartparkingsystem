def print(i):
    from signal import signal, SIGTERM, SIGHUP, pause
    from rpi_lcd import LCD
    lcd = LCD()
    def safe_exit(signum, frame):
        exit(1)
    try:
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
        lcd.text("Welcome.", 1)
        if(i==0):
            text = "No space." + i 
        else:
            text = "Park at slot: " + i 
        lcd.text(text, 2)
        pause()
    except KeyboardInterrupt:
        pass
    finally:
        pass