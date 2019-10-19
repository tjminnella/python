import time

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


kit.servo[2].angle = 120
kit.servo[3].angle = 45
kit.servo[4].angle = 0
kit.servo[5].angle = 0
kit.servo[6].angle = 0
time.sleep(1)
kit.servo[3].angle = 0
kit.servo[4].angle = 180
kit.servo[5].angle = 180
kit.servo[6].angle = 180
time.sleep(1)
kit.servo[3].angle = 45
kit.servo[4].angle = 0
kit.servo[5].angle = 0
kit.servo[6].angle = 0
time.sleep(1)
kit.servo[3].angle = 0
kit.servo[4].angle = 180
kit.servo[5].angle = 180
kit.servo[6].angle = 180
time.sleep(1)
kit.servo[3].angle = 45
kit.servo[4].angle = 0
kit.servo[5].angle = 0
kit.servo[6].angle = 0
time.sleep(1)

kit.servo[1].angle = 120
kit.servo[2].angle = 120
kit.servo[3].angle = 0
kit.servo[4].angle = 90
kit.servo[5].angle = 90
kit.servo[6].angle = 0

time.sleep(1)

kit.servo[1].angle = 120
kit.servo[2].angle = 110
kit.servo[3].angle = 0
kit.servo[4].angle = 180
kit.servo[5].angle = 90
kit.servo[6].angle = 180

time.sleep(.5)

kit.servo[4].angle = 0
time.sleep(.5)
kit.servo[4].angle = 180
time.sleep(.5)
kit.servo[5].angle = 0
time.sleep(.5)
kit.servo[4].angle = 180
time.sleep(.5)
kit.servo[4].angle = 0
time.sleep(.5)
kit.servo[4].angle = 180
time.sleep(.5)
kit.servo[4].angle = 0
time.sleep(.5)
kit.servo[4].angle = 90

time.sleep(.5)

kit.servo[5].angle = 0
time.sleep(.5)
kit.servo[5].angle = 180
time.sleep(.5)
kit.servo[5].angle = 0
time.sleep(.5)
kit.servo[5].angle = 180
time.sleep(.5)
kit.servo[5].angle = 0
time.sleep(.5)
kit.servo[5].angle = 180
time.sleep(.5)
kit.servo[5].angle = 0
time.sleep(.5)
kit.servo[5].angle = 90

time.sleep(.5)

kit.servo[6].angle = 0
time.sleep(.5)
kit.servo[6].angle = 180
time.sleep(.5)
kit.servo[6].angle = 0
time.sleep(.5)
kit.servo[6].angle = 180
time.sleep(.5)
kit.servo[6].angle = 0
time.sleep(.5)
kit.servo[6].angle = 180
time.sleep(.5)
kit.servo[6].angle = 0
time.sleep(.5)
kit.servo[6].angle = 90


time.sleep(.5)

kit.servo[1].angle = 140
time.sleep(.5)
kit.servo[1].angle = 100
time.sleep(.5)
kit.servo[1].angle = 140
time.sleep(.5)
kit.servo[1].angle = 100
time.sleep(.5)
kit.servo[1].angle = 140
time.sleep(.5)
kit.servo[1].angle = 100
time.sleep(.5)
kit.servo[1].angle = 140
time.sleep(.5)
kit.servo[1].angle = 100
time.sleep(.5)
kit.servo[1].angle = 140
time.sleep(.5)
kit.servo[1].angle = 120

time.sleep(1)

kit.servo[1].angle = 120
kit.servo[2].angle = 100
kit.servo[3].angle = 20
kit.servo[4].angle = 0
kit.servo[5].angle = 90
kit.servo[6].angle = 0

time.sleep(1)

kit.servo[1].angle = 120
kit.servo[2].angle = 90
kit.servo[3].angle = 30
kit.servo[4].angle = 180
kit.servo[5].angle = 90
kit.servo[6].angle = 180

time.sleep(1)

kit.servo[1].angle = 120
kit.servo[2].angle = 20
kit.servo[3].angle = 0
kit.servo[4].angle = 0
kit.servo[5].angle = 90
kit.servo[6].angle = 0

time.sleep(1)

kit.servo[1].angle = 120
kit.servo[2].angle = 120
kit.servo[3].angle = 0
kit.servo[4].angle = 90
kit.servo[5].angle = 90
kit.servo[6].angle = 180

time.sleep(1)

kit.servo[1].angle = 120
kit.servo[2].angle = 110
kit.servo[3].angle = 0
kit.servo[4].angle = 90
kit.servo[5].angle = 90
kit.servo[6].angle = 90
