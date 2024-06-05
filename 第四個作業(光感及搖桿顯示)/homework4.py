import sys
import time
import smbus2
import spidev
import os
from RPLCD.i2c import CharLCD

#LCD
sys.modules['smbus'] = smbus2
lcd = CharLCD('PCF8574', address=0x3f, port=1, backlight_enabled=True)


# open(bus, device) : open(X,Y) will open /dev/spidev-X.Y
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

#Light
# Read SPI data from MCP3008, Channel must be an integer 0-7
def ReadADC(ch):
    if ((ch > 7) or (ch < 0)):
       return -1
    adc = spi.xfer2([1,(8+ch)<<4,0])
    # print(str(adc[0])+"\n")
    # print(str(adc[1])+"\n")
    # print(str(adc[2])+"\n")
    data = ((adc[1]&3)<<8) + adc[2]
    return data

# Convert data to voltage level
def ReadVolts(data,deci):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,deci)
    return volts

# Calculate temperature from LM35 data
def ConvertTemp(data,deci):
    temp = data * 100
    temp = round(temp,deci)
    return temp

# Define sensor channels
light_ch = 0
temp_ch  = 1

# Define delay between readings
delay = 1

#joystick
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Define sensor channels
# (channels 3 to 7 unused)
swt_channel = 0
vrx_channel = 1
vry_channel = 1


try:
    print('Press CTRL + C to quit')
    lcd.clear()
    while True:
        # Read the joystick position data
        vrx_pos = ReadChannel(vrx_channel)
        vry_pos = ReadChannel(vry_channel)

        # Read switch state
        swt_val = ReadChannel(swt_channel)

        light_data = ReadADC(light_ch)
        light_volts = ReadVolts(light_data,2)

        lcd.cursor_pos = (0, 0)
        # lcd.write_string(" 123456789abcdef")
        lcd.write_string("Light:{}({:.2f}V)".format(light_data, light_volts))
        lcd.cursor_pos = (1, 0)
        lcd.write_string("X:{}/Y:{}/Z:{}---".format(vrx_pos,vry_pos,swt_val))
        time.sleep(1)
except KeyboardInterrupt:
    print('Closed Program')
finally:
    lcd.clear()