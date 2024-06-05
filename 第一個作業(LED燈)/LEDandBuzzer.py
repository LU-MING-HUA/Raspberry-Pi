import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

while True:
    #first
    led1 = 18
    GPIO.setup(led1,GPIO.OUT)
    GPIO.output(led1,1)
    sleep(60)
    GPIO.output(led1,0)

    #second
    led2 = 27
    GPIO.setup(led2,GPIO.OUT)
    buzzer = 17
    GPIO.setup(buzzer,GPIO.OUT)
    for i in range(5):
        GPIO.output(led2,1)
        GPIO.output(buzzer,True)
        sleep(1)
        GPIO.output(led2,0)
        GPIO.output(buzzer,False)
        sleep(1)

    #third
    led3 = 22
    GPIO.setup(led3,GPIO.OUT)
    GPIO.output(led3,1)
    sleep(60)
    GPIO.output(led3,0)

    #fourth
    for i in range(3):
        GPIO.output(led2,1)
        GPIO.output(buzzer,True)
        sleep(1)
        GPIO.output(led2,0)
        GPIO.output(buzzer,False)
        sleep(1)

GPIO.cleanup()
