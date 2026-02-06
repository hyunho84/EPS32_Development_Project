from machine import Pin
from config.settings import LED_PIN, LED_COUNT
import neopixel
import time

class Cjmcu_Led:
  def __init__(self):
    print("Cjmcu Led __init__ Start")
    self.neo = neopixel.NeoPixel(Pin(LED_PIN, Pin.OUT), LED_COUNT)
    self.clear()

  def clear(self):
    for i in range(LED_COUNT):
      self.neo[i] = (0, 0, 0)
    self.neo.write()
  
  def led_grean_on(self, led_count):
    for i in range(led_count):
      self.neo[i] = (0, 50, 0)    # (R, G, B)
      self.neo.write()
      time.sleep(0.05)
    
    time.sleep(0.5)
    self.clear()
    time.sleep(0.5)

