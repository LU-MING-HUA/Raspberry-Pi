# 很吵的東西 我也不知道該怎麼解釋

import RPi.GPIO as gpio
import time
#              do   re   mi   fa   so   la   si   do
piano = list([261, 293, 329, 349, 391, 440, 493, 523])
buzzer = 18

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(buzzer, gpio.OUT)


def play(pitch, sec):
    half_pitch = (1 / pitch) / 2
    t = int(pitch * sec)
    for i in range(t):
        gpio.output(buzzer, gpio.HIGH)
        time.sleep(half_pitch)
        gpio.output(buzzer, gpio.LOW)
        time.sleep(half_pitch)


for p in piano:
    play(1, 1)
    play(2, 1)
    play(3, 1)
    play(4, 1)
    play(5, 1)
    play(6, 1)
    play(7, 1)
    play(8, 1)
    

gpio.cleanup()