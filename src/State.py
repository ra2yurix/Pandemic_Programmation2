from enum import Enum, unique


@unique
class State(Enum):
    SUSCEPTIBLE, INFECTED, RECOVERED, DEAD = range(4)

