#!/usr/bin/env python3

import tkinter
from Simulator import Simulator

def main():
    root = tkinter.Tk()
    root.title('Brownian Motion Simulation')
    simulator = Simulator(root,50,60,2)
    simulator.simulate(300)
    root.mainloop()

if __name__ == '__main__':
    main()
