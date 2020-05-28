import Field
from Location import Velocity, Location


class Sapiens:
    """Represents a Sapiens in movement with a location
    and a velocity.
s
    :author: Peter Sander
    :author: ZHENG Yannan
    """

    def __init__(self, location: Location, velocity: Velocity,
                 colour: str, field: Field):
        """Initialize a Sapiens.

        :colour: Sapiens colour.
        :field: Field containing the Sapiens.
        """
        self.location = location
        self.velocity = velocity
        self.colour = colour
        self.field = field

    def move(self) -> None:
        """Sapiens moves to a new location.

        Random move depending on the Sapiens's current location.
        """
        nextLocation = self.field.freeAdjacentLocation(self, 2)
        self.setLocation(nextLocation)

    def setLocation(self, nextLocation: Location) -> None:
        """Place the Sapiens at the given location.
        """
        self.field.clear(self.location)
        self.location = nextLocation
        self.field.place(self)

    def __str__(self):
        return f'Sapiens({self.location})'
