import random
import time
from Field import Field
from Sapiens import Sapiens
from Location import Velocity, Location
from Randomizer import Randomizer
from SimulatorView import SimulatorView


class Simulator():
    """Runs the brownian-motion simulation.

    :author: Peter Sander
    :author: ZHENG Yannan
    """

    def __init__(self, root: object, size=50, num_Sapien=50):
        """Create a simulation with the given field size.

        :root: tkinter.Tk graphics object
        """
        self.size = size
        self._Sapiens = []  # all Sapiens in the simulation
        self._field = Field(size)
        self.step = 0
        self._view = SimulatorView(root, size)
        self._colours = ('red', 'green', 'blue', 'yellow', 'magenta', 'cyan')
        self.reset(num_Sapien)

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
        #  all _Sapiens in motion
        for Sapiens in self._Sapiens:
            Sapiens.move()
        self._view.showStatus(self.step, self._Sapiens)

    def reset(self, num_Sapien):
        """Reset the simulation to a starting location.
        """
        self.step = 0
        self._Sapiens = []
        self.populate(num_Sapien)
        self._view.showStatus(self.step, self._Sapiens)

    def populate(self, num_Sapien=50):
        """Populates the _field with randomly-locationed _Sapiens.
        """
        self._field.clear()
        for p in range(num_Sapien):
            location = Location(max=self.size)  # generate 0 <= random Location < size
            velocity = Velocity()
            color = self._colours[random.randint(0, self._colours.__len__() - 1)]
            Sapien_new = Sapiens(location, velocity, color, self._field)
            self._Sapiens.append(Sapien_new)
            # generate random -1 <= random Velocity < 1
            # store Sapiens with location and velocity
