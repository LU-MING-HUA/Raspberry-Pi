import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
buzzer = 18
GPIO.setup(buzzer,GPIO.OUT)

while True:
   GPIO.output(buzzer,True)
   sleep(2) 
   GPIO.output(buzzer,False)
   sleep(2)
