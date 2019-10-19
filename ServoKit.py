import time

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


kit.servo[1].angle = 120
kit.servo[2].angle = 120
kit.servo[3].angle = 0
kit.servo[4].angle = 90
time.sleep(1)
kit.servo[1].angle = 120
kit.servo[2].angle = 120
kit.servo[3].angle = 5
time.sleep(1)
kit.servo[3].angle = 10
time.sleep(1)
kit.servo[3].angle = 20
time.sleep(1)
kit.servo[3].angle = 25
time.sleep(1)
kit.servo[3].angle = 30
time.sleep(.5)
kit.servo[3].angle = 35
time.sleep(.5)
kit.servo[3].angle = 10
time.sleep(.5)
kit.servo[3].angle = 35
time.sleep(.5)
kit.servo[3].angle = 30
time.sleep(.5)
kit.servo[3].angle = 15
time.sleep(.5)
kit.servo[3].angle = 10
time.sleep(.5)
kit.servo[3].angle = 25
time.sleep(.5)
kit.servo[3].angle = 30
time.sleep(.5)
kit.servo[3].angle = 40
time.sleep(.5)
kit.servo[3].angle = 30
time.sleep(.5)
kit.servo[3].angle = 20
time.sleep(.5)
kit.servo[3].angle = 0
time.sleep(.5)
kit.servo[3].angle = 20
time.sleep(.5)
kit.servo[3].angle = 30
time.sleep(.5)
kit.servo[3].angle = 2
time.sleep(.5)
kit.servo[3].angle = 10
time.sleep(.5)
kit.servo[3].angle = 25
time.sleep(.5)
kit.servo[3].angle = 30
time.sleep(.5)
kit.servo[3].angle = 35
time.sleep(.5)
kit.servo[3].angle = 40
time.sleep(.5)
kit.servo[3].angle = 45

kit.servo[1].angle = 90
kit.servo[2].angle = 100
kit.servo[3].angle = 10
kit.servo[4].angle = 20
time.sleep(1)
kit.servo[1].angle = 80
kit.servo[2].angle = 90
kit.servo[3].angle = 8
time.sleep(1)
kit.servo[2].angle = 80
kit.servo[3].angle = 7
time.sleep(1)
kit.servo[1].angle = 90
kit.servo[2].angle = 70
kit.servo[3].angle = 6
time.sleep(1)
kit.servo[2].angle = 70
kit.servo[3].angle = 6
time.sleep(1)
kit.servo[1].angle = 100
kit.servo[2].angle = 70
kit.servo[3].angle = 20
kit.servo[4].angle = 20
time.sleep(1)
kit.servo[2].angle = 70
kit.servo[3].angle = 0
time.sleep(1)
kit.servo[1].angle = 110
kit.servo[2].angle = 70
kit.servo[3].angle = 10
time.sleep(1)
kit.servo[2].angle = 70
kit.servo[3].angle = 0
time.sleep(1)
kit.servo[1].angle = 120
kit.servo[2].angle = 70
kit.servo[3].angle = 20
kit.servo[4].angle = 120
time.sleep(1)
kit.servo[2].angle = 70
kit.servo[3].angle = 0
time.sleep(1)
kit.servo[1].angle = 110
kit.servo[2].angle = 70
kit.servo[3].angle = 30
time.sleep(1)
kit.servo[2].angle = 70
kit.servo[3].angle = 0
time.sleep(1)
kit.servo[1].angle = 100
kit.servo[2].angle = 70
kit.servo[3].angle = 40
time.sleep(1)
kit.servo[2].angle = 70
kit.servo[3].angle = 0
time.sleep(1)
kit.servo[2].angle = 70
kit.servo[3].angle = 50
kit.servo[4].angle = 20
time.sleep(1)
kit.servo[2].angle = 70
kit.servo[3].angle = 0
time.sleep(1)
kit.servo[2].angle = 80
kit.servo[3].angle = 60
time.sleep(1)
kit.servo[1].angle = 120
kit.servo[2].angle = 70
kit.servo[3].angle = 0
time.sleep(1)
kit.servo[2].angle = 60
kit.servo[3].angle = 70
time.sleep(1)
kit.servo[2].angle = 50
kit.servo[3].angle = 0
kit.servo[4].angle = 30
time.sleep(1)
kit.servo[2].angle = 40
kit.servo[3].angle = 80
kit.servo[4].angle = 120
time.sleep(1)
kit.servo[2].angle = 80
kit.servo[3].angle = 80
time.sleep(1)
kit.servo[2].angle = 80
kit.servo[3].angle = 60
time.sleep(1)
kit.servo[2].angle = 50
kit.servo[3].angle = 30
time.sleep(1)
kit.servo[2].angle = 30
kit.servo[3].angle = 30
kit.servo[4].angle = 150
time.sleep(1)
kit.servo[2].angle = 20
kit.servo[3].angle = 0
time.sleep(1)
kit.servo[2].angle = 10
kit.servo[3].angle = 90
kit.servo[4].angle = 10
time.sleep(1)
kit.servo[2].angle = 40
kit.servo[3].angle = 30
time.sleep(1)
kit.servo[2].angle = 30
kit.servo[3].angle = 30
time.sleep(1)
kit.servo[2].angle = 40
kit.servo[3].angle = 40
time.sleep(1)
kit.servo[1].angle = 120
kit.servo[2].angle = 100
kit.servo[3].angle = 10
kit.servo[4].angle = 90
time.sleep(1)
kit.servo[1].angle = 120
kit.servo[2].angle = 110
kit.servo[3].angle = 10
kit.servo[4].angle = 90
time.sleep(1)
kit.servo[1].angle = 120
kit.servo[2].angle = 120
kit.servo[3].angle = 10
kit.servo[4].angle = 90
time.sleep(1)
kit.servo[1].angle = 120
kit.servo[2].angle = 120
kit.servo[3].angle = 0
kit.servo[4].angle = 90

# kit.servo[0].angle = 0




# With a standard servo, you specify the position as an angle.
# The angle will always be between 0 and the actuation
# range. The default is 180 degrees but your servo may have a smaller sweep.
# You can change the total angle by setting
# kit.servo[0].actuation_range = 160

# kit.servo[0].set_pulse_width_range(1000, 2000)

# kit.continuous_servo[1].throttle = 1
# kit.continuous_servo[1].throttle = -1
# kit.continuous_servo[1].throttle = 0.5
# kit.continuous_servo[1].throttle = 0
# for i in range(len(kit.servo)):
#      kit.continuous_servo[i].throttle = 0
# time.sleep(1)
