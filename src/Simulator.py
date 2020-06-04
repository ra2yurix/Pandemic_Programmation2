import random
import time
from Field import Field
from Sapiens import Sapiens
from Location import Velocity, Location
from Randomizer import Randomizer
from SimulatorView import SimulatorView
from State import State
import Stats
import Virus

class Simulator():
    """Runs the brownian-motion simulation.

    :author: Peter Sander
    :author: ZHENG Yannan
    """

    def __init__(self, root: object, size=50, num_sapiens=50,num_infected=20):
        """Create a simulation with the given field size.

        :root: tkinter.Tk graphics object
        """
        self.size = size
        self._sapiens = []  # all sapiens in the simulation
        self._field = Field(size)
        Stats.step = 0
        self._view = SimulatorView(root, size)
        #self._colours = ('red', 'green', 'blue', 'yellow', 'magenta', 'cyan')
        self.colours = {State.SUSCEPTIBLE: 'slate blue',
                        State.INFECTED: 'red',
                        State.RECOVERED: 'spring green',
                        State.DEAD: 'black'}
        Stats.I = num_infected
        Stats.S = num_sapiens - num_infected
        Stats.I0 = Stats.I
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

        Stats.step = 1
        while Stats.step <= numSteps:
            if Stats.isViable()==True:
                self.simulateOneStep()
                Stats.I0 = Stats.I

            time.sleep(delay)

    def simulateOneStep(self) -> None:
        """Run the simulation from its current state for a single step.
        """
        Stats.step += 1
        #  all _sapiens in motion
        for Sapiens in self._sapiens:
            if Stats.step == Sapiens.r_or_d:
                Sapiens.if_I_die()
            if Sapiens.colour != 'black':
                Sapiens.move()
        self._view.showStatus(Stats.step, self._sapiens)


    def reset(self, num_sapiens):
        """Reset the simulation to a starting location.
        """
        Stats.step = 0
        self._sapiens = []
        self.populate(num_sapiens)
        self._view.showStatus(Stats.step, self._sapiens)

    def populate(self, num_sapiens=50):
        """Populates the _field with randomly-locationed _sapiens.
        """
        self._field.clear()
        for p in range(Stats.S):
            location = Location(max=self.size)  # generate 0 <= random Location < size
            velocity = Velocity()
            #color = self._colours[random.randint(0, self._colours.__len__() - 1)]
            color = self.colours[State.SUSCEPTIBLE];
            Sapien_new = Sapiens(location, velocity, color, self._field)
            self._sapiens.append(Sapien_new)
            # generate random -1 <= random Velocity < 1
            # store sapiens with location and velocity
        for p in range(Stats.I):
            location = Location(max=self.size)
            velocity = Velocity()
            color = self.colours[State.INFECTED];
            Sapien_new = Sapiens(location, velocity, color, self._field)
            Sapien_new.r_or_d = Virus.RECOVERY_TIME
            self._sapiens.append(Sapien_new)
