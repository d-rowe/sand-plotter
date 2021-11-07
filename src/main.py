from math import pi
from Plotter import Plotter


def main():
    plotter = Plotter()
    plotter.home()
    plotter.move_to(2 * pi, 1)


if __name__ == '__main__':
    main()
