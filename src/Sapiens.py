import Field
from Location import Velocity, Location
from State import State

class Sapiens:
    """Represents a sapiens in movement with a location
    and a velocity.
s
    :author: Peter Sander
    :author: ZHENG Yannan
    """

    def __init__(self, location: Location, velocity: Velocity,
                 colour: str, field: Field, state = State.SUSCEPTIBLE):
        """Initialize a sapiens.

        :colour: sapiens colour.
        :field: Field containing the sapiens.
        """
        self.location = location
        self.velocity = velocity
        self.colour = colour
        self.field = field
        self.state = state
        self.numberInfected = 0

    def move(self) -> None:
        """sapiens moves to a new location.

        Random move depending on the sapiens's current location.
        """
        nextLocation = self.field.freeAdjacentLocation(self, 2)
        self.setLocation(nextLocation)

    def setLocation(self, nextLocation: Location) -> None:
        """Place the sapiens at the given location.
        """
        self.field.clear(self.location)
        self.location = nextLocation
        self.field.place(self)

    def __str__(self):
        return f'Sapiens({self.location})'
