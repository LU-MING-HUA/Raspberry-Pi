import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 18
GPIO.setup(led,GPIO.OUT)



while True:
   GPIO.output(led,0)
   sleep(1) 
   GPIO.output(led,1)
   sleep(1)


GPIO.cleanup()
