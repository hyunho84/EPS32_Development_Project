# ESP32 Project
# Step Motor Control Test

from drivers.stepper_motor import StepperMotor
from drivers.jmod_temp_sensor import JmodTempSensor
from drivers.cjmcu_led import Cjmcu_Led
from services.motor_controller import StepperController
import uasyncio as asyncio
import time

print("ESP32 Step Motor Test")

motor = StepperMotor()
step_motor_controller = StepperController(motor)
temp = JmodTempSensor()
led_lamp = Cjmcu_Led()

async def main():
  print("Task 시작")
  asyncio.create_task(step_motor_controller.motor_task())

  print("1차 이동 시작")
  step_motor_controller.move(200, direction=1)   # 왼쪽
  # await asyncio.sleep(2)    # 필요할 때 사용 가능
  await step_motor_controller.wait_until_done()
  print("1차 이동 완료")

  # await asyncio.sleep(2)    # 필요할 때 사용 가능
  # await asyncio.sleep_ms(50)

  print("2차 이동 시작")
  # step_motor_controller.move(200, direction=1)   # 왼쪽
  step_motor_controller.move(200, direction=-1)  # 오른쪽
  await step_motor_controller.wait_until_done()
  print("2차 이동 완료")

asyncio.run(main())