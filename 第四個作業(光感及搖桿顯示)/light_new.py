import spidev
import time
import os

# open(bus, device) : open(X,Y) will open /dev/spidev-X.Y
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

# Read SPI data from MCP3008, Channel must be an integer ch0-7
def ReadADC(ch):
    if ((ch > 7) or (ch < 0)):
       return -1
    adc = spi.xfer2([1,(8+ch)<<4,0])
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
delay = 3
 
while True:
  # Read the light sensor data
  light_data = ReadADC(light_ch)
  light_volts = ReadVolts(light_data,2)
  temp_data = ReadADC(temp_ch)
  temp_volts = ReadVolts(temp_data,2)
  # Print out results
  print ("Light : ",light_data," (",light_volts,")")
  print ("temp : ",temp_data," (",temp_volts,")")

  # Delay seconds
  time.sleep(delay)
