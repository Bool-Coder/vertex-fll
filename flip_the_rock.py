
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# SETTINGS
MOTOR_SPEED = 500
SERVO_SPEED = 1200

# INITIALIZATION
hub = PrimeHub()

motor_left = Motor(Port.A)
motor_right = Motor(Port.B)

servo_left = Motor(Port.C)
servo_right = Motor(Port.D)


def setup():
    servo_left.control.limits(
        speed=2000,
        acceleration=5000
    )


def move(speed):
    motor_left.run(speed)
    motor_right.run(speed)

    wait(650)

    motor_left.stop()
    motor_right.stop()

def flip_servo(angle):
    servo_left.run_angle(
        speed=2000,
        rotation_angle=angle,
        then=Stop.HOLD
    )


def phase_1():
    flip_servo(1500)
    move(MOTOR_SPEED)
    flip_servo(-1500)

def phase_2():
    move(-MOTOR_SPEED)
    flip_servo(1550)
    move(MOTOR_SPEED)
    flip_servo(-1550)

def main():
    setup()
    phase_1()
    phase_2()


main()
