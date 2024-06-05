import RPi.GPIO as GPIO
import time

Btn = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(Btn,GPIO.IN)
while True:
    if GPIO.input(Btn) == GPIO.LOW:  # 檢查按鈕是否被按下
        print("按下")
        time.sleep(1)
    else:
        print("放開")
        time.sleep(1)
        # button_pressed_time = time.time()
        # time.sleep(2)
        # if GPIO.input(Btn) == GPIO.LOW:
        #     if time.time() - button_pressed_time >= 2:
        #         print("偵測長按按鈕 停止播歌!")
        # else:
        #     print("已放開")