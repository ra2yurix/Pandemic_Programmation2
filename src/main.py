#!/usr/bin/env python3

import tkinter
from Simulator import Simulator


def main():
    root = tkinter.Tk()
    root.title('Brownian Motion Simulation')
    simulator = Simulator(root, 50)
    simulator.simulate(300, 0.3)
    root.mainloop()


if __name__ == '__main__':
    main()
