#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
  if (GPIO.input(17) == 1):
    GPIO.output(4,False)
  else:
    GPIO.output(4,True)
