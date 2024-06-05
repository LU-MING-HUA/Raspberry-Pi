import RPi.GPIO as GPIO
import time
import sys
from RPLCD.i2c import CharLCD
import smbus2

Buzzer = 18 #音樂播放器
Btn_mode = 15 #控制模式用按鈕
Btn_end = 23
Btn_music1 = 21 #單音按鈕
Btn_music2 = 20
Btn_music3 = 16
Btn_music4 = 26
Btn_music5 = 19
Btn_music6 = 13
Btn_music7 = 6
music = [] #用於紀錄指導按鈕的串列
#按鈕顏色順序藍色 綠色 黃色 紅色 黑色 藍色 綠色
sys.modules['smbus'] = smbus2 #LCD要用

lcd = CharLCD('PCF8574', address=0x3f, port=1, backlight_enabled=True)

#          do   re   mi   fa   so   la   ci
CM = [0, 525, 589, 330, 350, 393, 441, 495] #混合 小蜜蜂
CM2 = [0, 262, 294, 330, 350, 393, 441, 495] #瑪莉有隻小綿羊
def btnMusicForLittleSheep(): #小綿羊的音調按鈕
    if GPIO.input(Btn_music1) == GPIO.HIGH:  # 檢查按鈕是否被按下
        Buzz.start(50)
        Buzz.ChangeFrequency(262)
        time.sleep(0.25)
        Buzz.stop()
        music.append(1)
    elif GPIO.input(Btn_music2) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(294)
        time.sleep(0.25)
        Buzz.stop()
        music.append(2)
    elif GPIO.input(Btn_music3) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(330)
        time.sleep(0.25)
        Buzz.stop()
        music.append(3)
    elif GPIO.input(Btn_music4) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(350)
        time.sleep(0.25)
        Buzz.stop()
        music.append(4)
    elif GPIO.input(Btn_music5) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(393)
        time.sleep(0.25)
        Buzz.stop()
        music.append(5)
    elif GPIO.input(Btn_music6) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(441)
        time.sleep(0.25)
        Buzz.stop()
        music.append(6)
    elif GPIO.input(Btn_music7) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(495)
        time.sleep(0.25)
        Buzz.stop()
        music.append(7)

def btnMusicForLittleBee(): #小蜜蜂的音調按鈕
    if GPIO.input(Btn_music1) == GPIO.HIGH:  # 檢查按鈕是否被按下
        Buzz.start(50)
        Buzz.ChangeFrequency(525)
        time.sleep(0.25)
        Buzz.stop()
        music.append(1)
    elif GPIO.input(Btn_music2) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(589)
        time.sleep(0.25)
        Buzz.stop()
        music.append(2)
    elif GPIO.input(Btn_music3) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(330)
        time.sleep(0.25)
        Buzz.stop()
        music.append(3)
    elif GPIO.input(Btn_music4) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(350)
        time.sleep(0.25)
        Buzz.stop()
        music.append(4)
    elif GPIO.input(Btn_music5) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(393)
        time.sleep(0.25)
        Buzz.stop()
        music.append(5)
    elif GPIO.input(Btn_music6) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(441)
        time.sleep(0.25)
        Buzz.stop()
        music.append(6)
    elif GPIO.input(Btn_music7) == GPIO.HIGH:
        Buzz.start(50)
        Buzz.ChangeFrequency(495)
        time.sleep(0.25)
        Buzz.stop()
        music.append(7)

def modeForBtnMusicLittleSheep(): #綿羊的音調按鈕+LCD面板指導
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("3212333222355")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Mode: btnMusic2")
    global music
    music = []
    while True:
        btnMusicForLittleSheep()
        if len(music) == 13 and music == [3, 2, 1, 2, 3, 3, 3, 2, 2, 2, 3, 5, 5]:
            print("完美彈奏 下一階段")
            break
        elif len(music) == 13 and music != [3, 2, 1, 2, 3, 3, 3, 2, 2, 2, 3, 5, 5]:
            print("彈奏有誤 再來一次")
            music = []
        if GPIO.input(Btn_mode) == GPIO.LOW:  # 檢查按鈕是否被按下
            button_pressed_time = time.time()
            time.sleep(3)
            if GPIO.input(Btn_mode) == GPIO.LOW:
                if time.time() - button_pressed_time >= 2:
                    print("更改模式")
                    return
        if GPIO.input(Btn_end) == GPIO.LOW: #檢查結束按鈕
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Turn Off")
            print("關機")
            sys.exit()

    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("321233322321")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Mode: btnMusic2")
    music = []
    while True:
        btnMusicForLittleSheep()
        if len(music) == 12 and music == [3, 2, 1, 2, 3, 3, 3, 2, 2, 3, 2, 1]:
            print("完美彈奏 下一階段")
            break
        elif len(music) == 12 and music != [3, 2, 1, 2, 3, 3, 3, 2, 2, 3, 2, 1]:
            print("彈奏有誤 再來一次")
            music = []
        if GPIO.input(Btn_mode) == GPIO.LOW:  # 檢查按鈕是否被按下
            button_pressed_time = time.time()
            time.sleep(3)
            if GPIO.input(Btn_mode) == GPIO.LOW:
                if time.time() - button_pressed_time >= 2:
                    print("更改模式")
                    return
        if GPIO.input(Btn_end) == GPIO.LOW: #檢查結束按鈕
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Turn Off")
            print("關機")
            sys.exit()

    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("End Good")

def modeForBtnMusicLittleBee(): #小蜜蜂的音調按鈕+LCD面板指導
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("2771665671222")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Mode: btnMusic1")
    global music
    music = []
    while True:
        btnMusicForLittleBee()
        if len(music) == 13 and music == [2, 7, 7, 1, 6, 6, 5, 6, 7, 1, 2, 2, 2]:
            print("完美彈奏 下一階段")
            break
        elif len(music) == 13 and music != [2, 7, 7, 1, 6, 6, 5, 6, 7, 1, 2, 2, 2]:
            print("彈奏有誤 再來一次")
            music = []
        if GPIO.input(Btn_mode) == GPIO.LOW:  # 檢查按鈕是否被按下
            button_pressed_time = time.time()
            time.sleep(3)
            if GPIO.input(Btn_mode) == GPIO.LOW:
                if time.time() - button_pressed_time >= 2:
                    print("更改模式")
                    return
        if GPIO.input(Btn_end) == GPIO.LOW: #檢查結束按鈕
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Turn Off")
            print("關機")
            sys.exit()

    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("27716657227")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Mode: btnMusic1")
    music = []
    while True:
        btnMusicForLittleBee()
        if len(music) == 11 and music == [2, 7, 7, 1, 6, 6, 5, 7, 2, 2, 7]:
            print("完美彈奏 下一階段")
            break
        elif len(music) == 11 and music != [2, 7, 7, 1, 6, 6, 5, 7, 2, 2, 7]:
            print("彈奏有誤 再來一次")
            music = []
        if GPIO.input(Btn_mode) == GPIO.LOW:  # 檢查按鈕是否被按下
            button_pressed_time = time.time()
            time.sleep(3)
            if GPIO.input(Btn_mode) == GPIO.LOW:
                if time.time() - button_pressed_time >= 2:
                    print("更改模式")
                    return
        if GPIO.input(Btn_end) == GPIO.LOW: #檢查結束按鈕
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Turn Off")
            print("關機")
            sys.exit()

    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("66666717777712")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Mode: btnMusic1")
    music = []
    i = 0
    while True:
        btnMusicForLittleBee()
        if len(music) == 14 and music == [6, 6, 6, 6, 6, 7, 1, 7, 7, 7, 7, 7, 1, 2]:
            print("完美彈奏 下一階段")
            break
        elif len(music) == 14 and music != [6, 6, 6, 6, 6, 7, 1, 7, 7, 7, 7, 7, 1, 2]:
            print("彈奏有誤 再來一次")
            music = []
        if GPIO.input(Btn_mode) == GPIO.LOW:  # 檢查按鈕是否被按下
            button_pressed_time = time.time()
            time.sleep(3)
            if GPIO.input(Btn_mode) == GPIO.LOW:
                if time.time() - button_pressed_time >= 2:
                    print("更改模式")
                    return
        if GPIO.input(Btn_end) == GPIO.LOW: #檢查結束按鈕
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Turn Off")
            print("關機")
            sys.exit()

    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("27716657225")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Mode: btnMusic1")
    music = []
    while True:
        btnMusicForLittleBee()
        if len(music) == 11 and music == [2, 7, 7, 1, 6, 6, 5, 7, 2, 2, 5]:
            print("完美彈奏 完成演出")
            break
        elif len(music) == 11 and music != [2, 7, 7, 1, 6, 6, 5, 7, 2, 2, 5]:
            print("彈奏有誤 再來一次")
            music = []
        if GPIO.input(Btn_mode) == GPIO.LOW:  # 檢查按鈕是否被按下
            button_pressed_time = time.time()
            time.sleep(3)
            if GPIO.input(Btn_mode) == GPIO.LOW:
                if time.time() - button_pressed_time >= 2:
                    print("更改模式")
                    return
        if GPIO.input(Btn_end) == GPIO.LOW: #檢查結束按鈕
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Turn Off")
            print("關機")
            sys.exit()
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("End Good")

def modeForAutoSony():
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
    time.sleep(2)
    while True:
        print('\nPlaying song 1...')
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("LittleBee")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Mode: AutoMusic1")
        for i in range(1, len(song_1)):
            if GPIO.input(Btn_mode) == GPIO.LOW:  # 檢查按鈕是否被按下
                button_pressed_time = time.time()
                time.sleep(3)
                if GPIO.input(Btn_mode) == GPIO.LOW:
                    if time.time() - button_pressed_time >= 2:
                        print("更改模式")
                        return
                stopSong()  # 如果按下按鈕，立即停止歌曲
                break
            if GPIO.input(Btn_end) == GPIO.LOW: #檢查結束按鈕
                lcd.clear()
                lcd.cursor_pos = (0, 0)
                lcd.write_string("Turn Off")
                print("關機")
                sys.exit()
            Buzz.start(50)
            Buzz.ChangeFrequency(song_1[i])
            time.sleep(beat_1[i] * 0.25)
            Buzz.stop()
            time.sleep(0.25)
        
        print('\nPlaying song 2...')
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("LittleSheep")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Mode: AutoMusic2")
        for i in range(1, len(song_2)):
            if GPIO.input(Btn_mode) == GPIO.LOW:  # 檢查按鈕是否被按下
                button_pressed_time = time.time()
                time.sleep(3)
                if GPIO.input(Btn_mode) == GPIO.LOW:
                    if time.time() - button_pressed_time >= 2:
                        print("更改模式")
                        return
                stopSong()  # 如果按下按鈕，立即停止歌曲
                break
            if GPIO.input(Btn_end) == GPIO.LOW: #檢查結束按鈕
                lcd.clear()
                lcd.cursor_pos = (0, 0)
                lcd.write_string("Turn Off")
                print("關機")
                sys.exit()
            Buzz.start(50)
            Buzz.ChangeFrequency(song_2[i])
            time.sleep(beat_2[i] * 0.25)
            Buzz.stop()
            time.sleep(0.25)

def setUp():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Buzzer, GPIO.OUT)
    GPIO.setup(Btn_mode, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Btn_end, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Btn_music1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Btn_music2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Btn_music3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Btn_music4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Btn_music5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Btn_music6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Btn_music7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global Buzz
    Buzz = GPIO.PWM(Buzzer, 440)
    lcd.clear()

def stopSong(): #停止歌曲
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
    setUp()
    try:
        while True:
            modeForBtnMusicLittleBee()
            modeForBtnMusicLittleSheep()
            modeForAutoSony()
    except KeyboardInterrupt:
        destroy()