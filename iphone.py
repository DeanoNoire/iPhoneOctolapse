#!/usr/bin python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = 12

GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(pin, GPIO.LOW)

time.sleep(0.5)

# Turn off the GPIO pin
GPIO.output(pin, GPIO.HIGH)

# Clean up GPIO
GPIO.cleanup()