from decimal import Decimal
from RpiMotorLib import RpiMotorLib
from constants import MOTOR_TYPE, STEP_TYPE_FULL, VERBOSE_MODE

MOTOR_NAME = "ArmMotor"
A11 = 19
A12 = 26
B11 = 21
B12 = 13
GPIO_PINS = [A11, B11, A12, B12]
STEPS_PER_MM = 5
LENGTH_IN_MM = 300


class Arm:
    motor = RpiMotorLib.BYJMotor(MOTOR_NAME, MOTOR_TYPE)
    current_rho: Decimal = 0

    def move_to(self, rho: Decimal):
        rho_delta = rho - self.current_rho
        if rho_delta == 0:
            return

        is_cc_wise = rho_delta >= 0
        wait = 0.5
        steps = abs(rho_delta) * LENGTH_IN_MM * STEPS_PER_MM
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
        self.current_rho = rho
