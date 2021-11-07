from decimal import Decimal
from Plotter import Plotter

TRACK_PATH = "temp.thr"


def main():
    plotter = Plotter()
    with open(TRACK_PATH) as f:
        for line in f:
            theta, rho = map(Decimal, line.split(" "))
            plotter.move_to(theta, rho)


if __name__ == '__main__':
    main()
