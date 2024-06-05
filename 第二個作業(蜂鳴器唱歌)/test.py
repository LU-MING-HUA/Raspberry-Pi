import RPi.GPIO as GPIO
import time

Buzzer = 18

# 小蜜蜂音樂樂譜和節拍
#          do   re   mi   fa   so   la   ci
CM = [ 0, 262, 294, 330, 350, 393, 441, 495 ]

song_1 = [ CM[1], 0, CM[2], 0, CM[3], 0, CM[4], 0, CM[5], 0, CM[6], 0, CM[7], 0]
beat_1 = [ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Buzzer, GPIO.OUT)
    global Buzz
    Buzz = GPIO.PWM(Buzzer, 440)
    Buzz.start(50)

def loop():
    while True:
        print('\nPlaying song 1...')
        for i in range(len(song_1)):
            if song_1[i] > 0:
                Buzz.ChangeFrequency(song_1[i])
            else:
                time.sleep(beat_1[i] * 0.5)  # 持續靜音的時間
                continue
            time.sleep(beat_1[i] * 0.5)
        time.sleep(10)
	

def destroy():
    Buzz.stop()
    GPIO.output(Buzzer, 1)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
