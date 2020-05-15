import random
import time
from Field import Field
from Particle import Particle
from Position import Direction, Position
from Randomizer import Randomizer
from SimulatorView import SimulatorView


class Simulator():
    """Runs the brownian-motion simulation.

    :author: Peter Sander
    :author: ZHENG Yannan
    """

    def __init__(self, root: object, size=50, num_particle=50):
        """Create a simulation with the given field size.

        :root: tkinter.Tk graphics object
        """
        self.size = size
        self._particles = []  # all particles in the simulation
        self._field = Field(size)
        self.step = 0
        self._view = SimulatorView(root, size)
        self._colours = ('red', 'green', 'blue', 'yellow', 'magenta', 'cyan')
        self.reset(num_particle)

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
        #  all _particles in motion
        for particle in self._particles:
            particle.move()
        self._view.showStatus(self.step, self._particles)

    def reset(self, num_particle):
        """Reset the simulation to a starting position.
        """
        self.step = 0
        self._particles = []
        self.populate(num_particle)
        self._view.showStatus(self.step, self._particles)

    def populate(self, num_particle=50):
        """Populates the _field with randomly-positioned _particles.
        """
        self._field.clear()
        for p in range(num_particle):
            position = Position(max=self.size)  # generate 0 <= random Position < size
            direction = Direction()
            color = self._colours[random.randint(0, self._colours.__len__() - 1)]
            particle_new = Particle(position, direction, color, self._field)
            self._particles.append(particle_new)
            # generate random -1 <= random Direction < 1
            # store particle with position and direction
