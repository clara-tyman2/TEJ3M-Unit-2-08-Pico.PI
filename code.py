
# Clara T
# Cretaed: April 9th 2025
# Move a servo with a potentiometer in sync

import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn

# create a PWMOut object on Pin 16.
pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)

potentionmeter = AnalogIn(board.GP26) # sets pot pin to pin 26/A0

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm, min_pulse = 650, max_pulse = 2500)

while True:
    print((potentionmeter.value))
    potVal = potentionmeter.value
    print(potVal)

    angle = potVal * (180/65535)
    my_servo.angle = angle
    time.sleep(0.05)