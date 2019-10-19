#!/user/bin/env python

import RPi.GPIO as GPIO
import time

pin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)

while True:
    input_value = GPIO.input(pin)
    if input_value == False:
        print("The button has been pressed")
        while input_value == False:
            input_value = GPIO.input(pin)
GPIO.cleanup()
