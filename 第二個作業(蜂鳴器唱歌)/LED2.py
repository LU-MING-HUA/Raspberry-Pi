#含按鈕
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led = 18
GPIO.setup(led,GPIO.OUT)
btn = 2
GPIO.setup(btn,GPIO.IN)
pre = 0

while True:
    state = GPIO.input(btn)
    if((not pre) and state):
        GPIO.output(led, True)
        sleep(3)
        GPIO.output(led, False)
    pre = state
    sleep(0.05)