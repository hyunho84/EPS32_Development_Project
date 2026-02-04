class Controller:
  def __init__(self, motor):
    self.motor = motor
    print("Controller __init__ Start")
  
  def rotate_left_once(self):
    self.motor.rotate_left()      # StepperMotor expected

  def rotate_right_once(self):
    self.motor.rotate_right()     # StepperMotor expected