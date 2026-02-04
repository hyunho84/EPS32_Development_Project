# ESP32 Project
# Step Motor Control Test

from drivers.stepper_motor import StepperMotor
from services.controller import Controller

print("ESP32 Step Motor Test")

motor = StepperMotor()
controller = Controller(motor)

i = 0

while i < 2:
  motor.rotate_left(512)
  motor.rotate_right(512)
  i += 1
  print(i)