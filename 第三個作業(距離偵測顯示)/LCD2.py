#在顯示器上顯示A~G 1~6
import sys
import time
import smbus2

sys.modules['smbus'] = smbus2

from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', address=0x3f, port=1, backlight_enabled=True)

try:
    print('Press CTRL + C to quit')
    lcd.clear()
    while True:
        lcd.cursor_pos = (0, 1)
        lcd.write_string("A")
        lcd.cursor_pos = (0, 2)
        lcd.write_string("B")
        lcd.cursor_pos = (0, 3)
        lcd.write_string("CDEFG")        
        lcd.cursor_pos = (1, 0)
        lcd.write_string("123456")
        time.sleep(1)
except KeyboardInterrupt:
        print('Closed Program')
finally:
    lcd.clear()