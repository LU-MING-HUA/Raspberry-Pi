#超音波+LCD+按鈕+蜂鳴器
#當按下按鈕時10秒內可以讓超音波偵測距離
#當距離低於10cm時蜂鳴器發出警告
#模擬倒車雷達等功能

#間斷超音波距離偵測

import time
import RPi.GPIO as GPIO
import smbus2
import sys
from RPLCD.i2c import CharLCD

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# 定義腳位
GPIO_TRIGGER = 23
GPIO_ECHO = 24
Btn = 21
Buzzer = 18
sys.modules['smbus'] = smbus2

print("超音波測量開始")
GPIO.setwarnings(False)
# 設定腳位輸入
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
GPIO.setup(Btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Buzzer, GPIO.OUT)
p = GPIO.PWM(Buzzer, 50)
lcd = CharLCD('PCF8574', address=0x3f, port=1, backlight_enabled=True)

# 起始設定超音波關閉脈波
GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle
# time.sleep(0.5)

try:
    while True:
        if GPIO.input(Btn) == GPIO.LOW:
            start_time = time.time() #計時器
            while time.time() - start_time <= 10:
                lcd.cursor_pos = (0, 0)
                GPIO.output(GPIO_TRIGGER, True)
                time.sleep(0.00001)
                GPIO.output(GPIO_TRIGGER, False)
                start = time.time()
                while GPIO.input(GPIO_ECHO) == 0:
                    start = time.time()
                while GPIO.input(GPIO_ECHO) == 1:
                    stop = time.time()

                elapsed = stop-start
                distance = elapsed * 340 *100 /2

                lcd.write_string("Distance(cm)")
                lcd.cursor_pos = (1, 0)
                lcd.write_string(str(distance))
                if distance <= 10.0:
                    print("過近")
                    p.start(50)
                    p.ChangeFrequency(523)
                else:
                    p.stop()
            
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string("End the detect")
            lcd.cursor_pos = (1, 0)
            lcd.write_string("Push the Btn")
except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()