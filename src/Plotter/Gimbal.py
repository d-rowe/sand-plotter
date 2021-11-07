from decimal import Decimal
from RpiMotorLib import RpiMotorLib
from constants import MOTOR_TYPE, STEP_TYPE_FULL, VERBOSE_MODE

MOTOR_NAME = "GimbalMotor"
A11 = 19
A12 = 26
B11 = 21
B12 = 13
GPIO_PINS = [A11, B11, A12, B12]
STEPS_PER_THETA = 10


class Gimbal:
    motor = RpiMotorLib.BYJMotor(MOTOR_NAME, MOTOR_TYPE)

    def move_to(self, theta: Decimal):
        wait = 0.5
        steps = STEPS_PER_THETA * theta
        cc_wise = False
        init_delay = 1
        self.motor.motor_run(
            GPIO_PINS,
            wait,
            steps,
            cc_wise,
            VERBOSE_MODE,
            STEP_TYPE_FULL,
            init_delay
        )
