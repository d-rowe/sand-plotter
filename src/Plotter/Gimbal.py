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
    current_theta: Decimal = 0

    def move_to(self, theta: Decimal):
        theta_delta = theta - self.current_theta
        if theta_delta == 0:
            return

        is_cc_wise = theta_delta >= 0
        wait = 0.5
        steps = abs(theta_delta) * STEPS_PER_THETA
        init_delay = 1
        self.motor.motor_run(
            GPIO_PINS,
            wait,
            steps,
            is_cc_wise,
            VERBOSE_MODE,
            STEP_TYPE_FULL,
            init_delay
        )
        self.current_theta = theta
