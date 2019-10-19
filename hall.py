#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#       Hall Effect Sensor
#
# This script tests the sensor on GPIO17.
#
# Author : Matt Hawkins
# Date   : 27/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import RPi.GPIO as GPIO
import time
import datetime

def sensorCallback1(channel):
  # Called if sensor output goes LOW
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  print "Sensor LOW " + stamp

def sensorCallback2(channel):
  # Called if sensor output goes HIGH
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  print "Sensor HIGH " + stamp

def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.
  print "main"
  try:
    # Loop until users quits with CTRL-C
    while True :
      print "sleep"
      time.sleep(0.1)
      print "wake"
      
  except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()  
  
# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

print "Setup GPIO pin as input"

# Set Switch GPIO as input
GPIO.setup(17 , GPIO.IN)
#GPIO.add_event_detect(17, GPIO.FALLING, callback=sensorCallback1)
#GPIO.add_event_detect(17, GPIO.RISING, callback=sensorCallback2)
GPIO.add_event_detect(17, GPIO.RISING, callback=sensorCallback2)
#GPIO.remove_event_detect(17)

if __name__=="__main__":
   main()
