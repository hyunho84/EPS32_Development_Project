# Step Motor [28BYJ-48] + [ULN2003]

STEPPER_PINS = [18, 19, 21, 22]

STEP_DELAY_MS = 8

STEP_SEQUENCE = [
  [1, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 0, 0, 1]
]