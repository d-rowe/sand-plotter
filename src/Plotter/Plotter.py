from decimal import Decimal
from Arm import Arm
from Gimbal import Gimbal


class Plotter:
    speed = 10  # mm/s
    arm = Arm()
    gimbal = Gimbal()

    def move_to(self, theta: Decimal, rho: Decimal):
        self.gimbal.move_to(theta)
        self.arm.move_to(rho)

    def set_speed(self, speed: Decimal):
        self.speed = speed
