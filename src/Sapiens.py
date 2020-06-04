import Field
from Location import Velocity, Location
from State import State
import Virus
import random
import Collisions
import Stats

class Sapiens:
    """Represents a sapiens in movement with a location
    and a velocity.
s
    :author: Peter Sander
    :author: ZHENG Yannan
    """

    def __init__(self, location: Location, velocity: Velocity,
                 colour: str, field: Field):
        """Initialize a sapiens.

        :colour: sapiens colour.
        :field: Field containing the sapiens.
        """
        self.location = location
        self.velocity = velocity
        self.colour = colour
        self.field = field
        self.numberInfected = 0
        self.r_or_d = -1

    def move(self) -> None:
        """sapiens moves to a new location.

        Random move depending on the sapiens's current location.
        """
        # nextLocation = self.field.freeAdjacentLocation(self, 2)
        nextLocation = Collisions.collisions(self, 2)
        self.setLocation(nextLocation)

    def setLocation(self, nextLocation: Location) -> None:
        """Place the sapiens at the given location.
        """
        self.field.clear(self.location)
        self.location = nextLocation
        self.field.place(self)

    def if_I_die(self):
        Stats.I = Stats.I-1
        if random.random()<=Virus.MORBIDITY_RATE:
            self.colour = 'black'
            Stats.D = Stats.D+1

        else:
            self.colour = 'spring green'
            Stats.R = Stats.R +1

    def __str__(self):
        return f'Sapiens({self.location})'
