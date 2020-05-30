import random
import time
from Field import Field
from Sapiens import Sapiens
from Location import Velocity, Location
from Randomizer import Randomizer
from SimulatorView import SimulatorView
from State import State

class Simulator():
    """Runs the brownian-motion simulation.

    :author: Peter Sander
    :author: ZHENG Yannan
    """

    def __init__(self, root: object, size=50, num_sapiens=50):
        """Create a simulation with the given field size.

        :root: tkinter.Tk graphics object
        """
        self.size = size
        self._sapiens = []  # all sapiens in the simulation
        self._field = Field(size)
        self.step = 0
        self._view = SimulatorView(root, size)
        #self._colours = ('red', 'green', 'blue', 'yellow', 'magenta', 'cyan')
        self.colours = {State.SUSCEPTIBLE: 'slate blue',
                        State.INFECTED: 'red',
                        State.RECOVERED: 'spring green',
                        State.DEAD: 'black'}
        self.reset(num_sapiens)

    def runLongSimulation(self) -> None:
        """Run the simulation from its current state for a reasonably
        long period, e.g. 500 steps.
        """
        self.simulate(500)

    def simulate(self, numSteps, delay=1) -> None:
        """Run the simulation from its current state for
        the given number of steps.

        :delay: Time (in secs) between each iteration.
        """

        self.step = 1
        while self.step <= numSteps:
            self.simulateOneStep()
            # self.step += 1
            time.sleep(delay)

    def simulateOneStep(self) -> None:
        """Run the simulation from its current state for a single step.
        """
        self.step += 1
        #  all _sapiens in motion
        for Sapiens in self._sapiens:
            Sapiens.move()
        self._view.showStatus(self.step, self._sapiens)

    def reset(self, num_sapiens):
        """Reset the simulation to a starting location.
        """
        self.step = 0
        self._sapiens = []
        self.populate(num_sapiens)
        self._view.showStatus(self.step, self._sapiens)

    def populate(self, num_sapiens=50):
        """Populates the _field with randomly-locationed _sapiens.
        """
        self._field.clear()
        for p in range(num_sapiens-1):
            location = Location(max=self.size)  # generate 0 <= random Location < size
            velocity = Velocity()
            #color = self._colours[random.randint(0, self._colours.__len__() - 1)]
            color = self.colours[State.SUSCEPTIBLE];
            Sapien_new = Sapiens(location, velocity, color, self._field)
            self._sapiens.append(Sapien_new)
            # generate random -1 <= random Velocity < 1
            # store sapiens with location and velocity

        #one infected
        location = Location(max=self.size)
        velocity = Velocity()
        color = self.colours[State.INFECTED];
        Sapien_new = Sapiens(location, velocity, color, self._field)
        self._sapiens.append(Sapien_new)
