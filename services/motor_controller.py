from config.settings import STEP_SEQUENCE, STEP_DELAY_MS, SLEEP_MS
import uasyncio as asyncio

class StepperController:
  def __init__(self, motor):
    self.motor = motor
    self.step_index = 0
    self.step = 0
    self.direction = 1    # 1 or -1 [1: 정방향 / -1: 역방향]
    self.running = False

    print("Stepper Motor Controller __init__ Start")
  
  def move(self, steps, direction=1):
    self.step = steps
    self.direction = direction
    self.running = True

  async def motor_task(self):
    while True:
      if self.running and self.step > 0:
        self.motor.motor_step(self.step_index)
        self.step_index = (self.step_index + self.direction) % len(STEP_SEQUENCE)
        self.step -= 1
        if self.step == 0:
          self.running = False
          print("motor_task_False")
          self.motor.motor_stop()
      else:
        self.running = False
      await asyncio.sleep_ms(STEP_DELAY_MS)
  
  async def wait_until_done(self):
    # running == False가 될때 까지 기다립니다.
    while self.running:
      await asyncio.sleep_ms(SLEEP_MS)