from machine import Pin, I2C
import time
from config.settings import I2C_SDA, I2C_SCL, I2C_FREQ, LM75A_ADRR

class JmodTempSensor:
  def __init__(self):
    print("Jmod Temp Sensor __init__ Start")
    self.i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=I2C_FREQ)

  def read_temp_sensor(self):
    raw = self.i2c.readfrom_mem(LM75A_ADRR, 0x00, 2)
    temp_raw = (raw[0] << 8 | raw[1]) >> 5
    
    if temp_raw & 0x400:
      temp_raw -= 1 << 11

    return temp_raw * 0.125