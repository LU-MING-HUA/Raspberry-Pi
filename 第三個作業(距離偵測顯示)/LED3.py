# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# Key connect to GPIO2
# LED connect to GPIO18
LED = 18
KEY = 2
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

ledStatus = True

def my_callback(channel):
    print("button pressed!")
    global ledStatus
    ledStatus = not ledStatus
    if ledStatus:
        GPIO.output(LED, GPIO.HIGH)
        pass
    else:
        GPIO.output(LED, GPIO.LOW)
        pass
    pass
    
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
#GPIO.add_event_detect(KEY, GPIO.RISING, callback=my_callback)
#GPIO.add_event_detect(KEY, GPIO.FALLING, callback=my_callback)
#GPIO.add_event_detect(KEY, GPIO.RISING, callback=my_callback, bouncetime=200)

GPIO.add_event_detect(KEY, GPIO.FALLING, callback=my_callback, bouncetime=200)

while True:
    try:
        print("I'm working...")
        time.sleep(5)
        pass
    except KeyboardInterrupt:
        break
        pass
    pass

GPIO.cleanup()