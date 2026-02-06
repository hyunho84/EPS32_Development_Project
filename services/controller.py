from config.settings import TEMP_THRESHOLD, LED_COUNT

class Controller:
  def __init__(self, motor, temp, led_lamp):
    self.motor = motor
    self.temp = temp
    self.led_lamp = led_lamp
    print("Controller __init__ Start")
  
  def rotate_left_once(self, step):
    self.motor.rotate_left(step)      # StepperMotor expected

  def rotate_right_once(self, step):
    self.motor.rotate_right(step)     # StepperMotor expected

  def check_temperature_and_act(self, temp_sensor, step):
    if temp_sensor >= TEMP_THRESHOLD:
      print(f"[Controller] 온도 {temp_sensor}°C → 모터 작동")
      self.rotate_left_once(step)
      self.rotate_right_once(step)
    else:
      print(f"[Controller] 온도 {temp_sensor}°C → 모터 정지")
  
  def led_on(self):
    self.led_lamp.led_grean_on(LED_COUNT)