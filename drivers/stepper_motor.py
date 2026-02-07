from machine import Pin
import time
from config.settings import STEPPER_PINS, STEP_DELAY_MS, STEP_SEQUENCE

class StepperMotor:
  def __init__(self):
    print("Stepper Motor __init__ Start")
  
    self.pins = []
    for pin in STEPPER_PINS:
      self.pins.append(Pin(pin, Pin.OUT))
      self.delay_ms = STEP_DELAY_MS
  
  def motor_step(self, step_index):
    for pin, value in zip(self.pins, STEP_SEQUENCE[step_index]):
      pin.value(value)
  
  def motor_stop(self):
    for pin in self.pins:
      pin.value(0)