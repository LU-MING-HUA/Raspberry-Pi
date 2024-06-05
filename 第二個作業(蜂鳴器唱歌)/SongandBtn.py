import RPi.GPIO as GPIO
import time
import sys

Buzzer = 18
Btn = 2




#          do   re   mi   fa   so   la   ci
CM = [0, 525, 589, 330, 350, 393, 441, 495] #混合 小蜜蜂
CM2 = [0, 262, 294, 330, 350, 393, 441, 495] #瑪莉有隻小綿羊


song_1 = [ CM[2], CM[7], CM[7], CM[1], CM[6], CM[6], CM[5], CM[6], CM[7], CM[1], CM[2], CM[2], CM[2], 
CM[2], CM[7], CM[7], CM[1], CM[6], CM[6], CM[5], CM[7], CM[2], CM[2], CM[7], 
CM[6], CM[6], CM[6], CM[6], CM[6], CM[7], CM[1], CM[7], CM[7], CM[7], CM[7], CM[7], CM[1], CM[2], 
CM[2], CM[7], CM[7], CM[1], CM[6], CM[6], CM[5], CM[7], CM[2], CM[2], CM[5]]

beat_1 = [ 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2,
 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 4,
 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2,
 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 4]

song_2 = [ CM2[3], CM2[2], CM2[1], CM2[2], CM2[3], CM2[3], CM2[3], CM2[2], CM2[2], CM2[2], CM2[3], CM2[5], CM2[5],
CM2[3], CM2[2], CM2[1], CM2[2], CM2[3], CM2[3], CM2[3], CM2[2], CM2[2], CM2[3], CM2[2], CM2[1]]

beat_2 = [ 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2,
1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2]


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Buzzer, GPIO.OUT)
    GPIO.setup(Btn,GPIO.IN)
    GPIO.setup(Btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global Buzz
    Buzz = GPIO.PWM(Buzzer, 440)

def stop_song():
    Buzz.stop()

def loop():
    while True:
        print('\nPlaying song 1...')
        for i in range(1, len(song_1)):
            if GPIO.input(Btn) == GPIO.LOW:  # 檢查按鈕是否被按下
                button_pressed_time = time.time()
                time.sleep(3)
                if GPIO.input(Btn) == GPIO.LOW:
                    if time.time() - button_pressed_time >= 2:
                        print("偵測長按按鈕 停止播歌!")
                        sys.exit()
                stop_song()  # 如果按下按鈕，立即停止歌曲
                break
            Buzz.start(50)
            Buzz.ChangeFrequency(song_1[i])
            time.sleep(beat_1[i] * 0.25)
            Buzz.stop()
            time.sleep(0.25)

        print('\nPlaying song 2...')
        for i in range(1, len(song_2)):
            if GPIO.input(Btn) == GPIO.LOW:  # 檢查按鈕是否被按下
                button_pressed_time = time.time()
                time.sleep(3)
                if GPIO.input(Btn) == GPIO.LOW:
                    if time.time() - button_pressed_time >= 2:
                        print("偵測長按按鈕 停止播歌!")
                        sys.exit()
                stop_song()  # 如果按下按鈕，立即停止歌曲
                break
            Buzz.start(50)
            Buzz.ChangeFrequency(song_2[i])
            time.sleep(beat_2[i] * 0.25)
            Buzz.stop()
            time.sleep(0.25)

	

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