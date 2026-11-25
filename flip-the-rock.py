from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

MOTOR_SPEED = 500
SERVO_SPEED = 1200

hub = PrimeHub()

motor_left = Motor(Port.A)
motor_right = Motor(Port.B)

servo_left = Motor(Port.C)
servo_right = Motor(Port.D)

#Phase 1

servo_left.control.limits(
    speed=2000,
    acceleration=5000
)

servo_left.run_angle(
    speed=2000,
    rotation_angle=1530,
    then=Stop.HOLD
)   

motor_left.run(MOTOR_SPEED)
motor_right.run(MOTOR_SPEED)

wait(650)

motor_left.stop()
motor_right.stop()


servo_left.run_angle(
    speed=2000,
    rotation_angle=-1530,
    then=Stop.HOLD
)

# Phase 2



motor_left.run(-MOTOR_SPEED)
motor_right.run(-MOTOR_SPEED)

wait(650)

motor_left.stop()
motor_right.stop()

servo_left.run_angle(
    speed=2000,
    rotation_angle=1700,
    then=Stop.HOLD
)

motor_left.run(MOTOR_SPEED)
motor_right.run(MOTOR_SPEED)

wait(650)

motor_left.stop()
motor_right.stop()


servo_left.run_angle(
    speed=2000,
    rotation_angle=-1700,
    then=Stop.HOLD
)   
