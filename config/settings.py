# Step Motor [28BYJ-48] + [ULN2003]

STEPPER_PINS = [25, 26, 27, 32]

STEP_DELAY_MS = 6

STEP_SEQUENCE = [
  [1, 0, 0, 0],
  [1, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [0, 0, 1, 0],
  [0, 0, 1, 1],
  [0, 0, 0, 1],
  [1, 0, 0, 1]
]

# JMOD - TEMP [LM75A]

I2C_SDA = 21
I2C_SCL = 22
I2C_FREQ = 100000       # 100KHZ Standard Mode

LM75A_ADRR = 0x48

TEMP_THRESHOLD = 23.5   # Temperature sensor Threshold