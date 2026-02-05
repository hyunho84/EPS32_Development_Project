# ESP32 Project
# Step Motor Control Test

from drivers.stepper_motor import StepperMotor
from drivers.jmod_temp_sensor import JmodTempSensor
from services.controller import Controller
import time

print("ESP32 Step Motor Test")

motor = StepperMotor()
temp = JmodTempSensor()
controller = Controller(motor, temp)

while True:
  temp_sensor = temp.read_temp_sensor()     # 온도 읽기
  
  if temp_sensor is not None:
    print("현재 온도는 {}도 입니다.".format(temp_sensor))
  else:
    print("경고: 센서 연결 상태를 확인해 주세요!")
  
  controller.check_temperature_and_act(temp_sensor, 512)

  time.sleep(1) 