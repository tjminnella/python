import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

def my_callback(channel):

    #print channel
    print GPIO.input(17)
    
    if GPIO.input(17):
        print "Rising Edge"
    else:
        print "Falling Edge"

GPIO.add_event_detect(17, GPIO.BOTH, callback=my_callback)

raw_input("press Enter when ready\n>")

try:
    sleep(30)
    print("DONE")
finally:
    GPIO.cleanup()
