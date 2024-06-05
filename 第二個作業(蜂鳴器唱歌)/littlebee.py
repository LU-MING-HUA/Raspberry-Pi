import RPi.GPIO as GPIO
import time

Buzzer = 18

# 小蜜蜂音樂樂譜和節拍
#          do   re   mi   fa   so   la   ci
# CM = [ 0, 262, 294, 330, 350, 393, 441, 495 ] #中
# CM = [0, 525, 589, 661, 700, 786, 882, 990] #高
CM = [0, 525, 589, 330, 350, 393, 441, 495] #混合

song_1 = [ CM[2], CM[7], CM[7], CM[1], CM[6], CM[6], CM[5], CM[6], CM[7], CM[1], CM[2], CM[2], CM[2], 
CM[2], CM[7], CM[7], CM[1], CM[6], CM[6], CM[5], CM[7], CM[2], CM[2], CM[7], 
CM[6], CM[6], CM[6], CM[6], CM[6], CM[7], CM[1], CM[7], CM[7], CM[7], CM[7], CM[7], CM[1], CM[2], 
CM[2], CM[7], CM[7], CM[1], CM[6], CM[6], CM[5], CM[7], CM[2], CM[2], CM[5]]
# beat_1 = [ 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4,
# 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 8,
# 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4,
# 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 8]
beat_1 = [ 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2,
 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 4,
 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2,
 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 4]

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
        for i in range(1, len(song_1)):
            Buzz.start(50)
            Buzz.ChangeFrequency(song_1[i])
            time.sleep(beat_1[i] * 0.25)
            Buzz.stop()
            time.sleep(0.25)
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
