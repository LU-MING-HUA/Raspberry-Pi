#播放do re mi

import time
import RPi.GPIO as GPIO

def doReMi(buzzerio):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzerio, GPIO.OUT)
    p = GPIO.PWM(buzzerio, 50)
    p.start(50)

    print("Do")
    p.ChangeFrequency(523)  # 523
    time.sleep(1)

    print("Re")
    p.ChangeFrequency(587)   #587
    time.sleep(1)
   
    print("Mi")
    p.ChangeFrequency(659)
    time.sleep(1)
    
    p.stop()
    GPIO.cleanup()

doReMi(18)
