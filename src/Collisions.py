import random
import Sapiens
from Location import Location
from Location import Velocity
import Virus
import Stats
from Randomizer import Randomizer


def collisions(Sapiens: Sapiens, radius: int) -> Location:
    """Try to find a free location that is adjacent to the given Sapiens's
    location.

    The returned location will be within the bounds of the field.
    :return: A valid location within the grid area, otherwise None.
    """
    next_pos = Location(Sapiens.location.row + Sapiens.velocity.row,
                        Sapiens.location.col + Sapiens.velocity.col)
    next_dir = Velocity(Sapiens.velocity.row, Sapiens.velocity.col)

    if next_pos.col <= 0 or next_pos.col >= Sapiens.field.size - 1:
        next_pos.col = Sapiens.location.col - next_dir.col
        next_dir.col = - next_dir.col
    if next_pos.row <= 0 or next_pos.row >= Sapiens.field.size - 1:
        next_pos.row = Sapiens.location.row - next_dir.row
        next_dir.row = -next_dir.row

    if Sapiens.field.getObjectAt(next_pos):
        if Sapiens.colour == 'red' and Sapiens.field._field[next_pos.row][
            next_pos.col].colour == 'slate blue' and random.random() <= Virus.INFECTION_RATE:
            Sapiens.field._field[next_pos.row][next_pos.col].colour = 'red'
            Sapiens.field._field[next_pos.row][next_pos.col].r_or_d = Stats.step + Virus.RECOVERY_TIME
            Sapiens.numberInfected = Sapiens.numberInfected + 1
            Stats.I = Stats.I + 1
            Stats.S = Stats.S - 1
        r = Sapiens.field._field[next_pos.row][next_pos.col].velocity.row
        c = Sapiens.field._field[next_pos.row][next_pos.col].velocity.col
        Sapiens.field._field[next_pos.row][next_pos.col].velocity.row = next_dir.row
        Sapiens.field._field[next_pos.row][next_pos.col].velocity.col = next_dir.col
        next_dir.row = r
        next_dir.col = c
        next_pos.row = Sapiens.location.row + next_dir.row
        next_pos.col = Sapiens.location.col + next_dir.col
    if Sapiens.field.getObjectAt(next_pos):
        if Sapiens.colour == 'red' and Sapiens.field._field[next_pos.row][
            next_pos.col].colour == 'slate blue' and random.random() <= Virus.INFECTION_RATE:
            Sapiens.field._field[next_pos.row][next_pos.col].colour = 'red'
            Sapiens.field._field[next_pos.row][next_pos.col].r_or_d = Stats.step + Virus.RECOVERY_TIME
            Sapiens.numberInfected = Sapiens.numberInfected + 1
            Stats.I = Stats.I + 1
            Stats.S = Stats.S - 1
        r = Sapiens.field._field[next_pos.row][next_pos.col].velocity.row
        c = Sapiens.field._field[next_pos.row][next_pos.col].velocity.col
        Sapiens.field._field[next_pos.row][next_pos.col].velocity.row = next_dir.row
        Sapiens.field._field[next_pos.row][next_pos.col].velocity.col = next_dir.col
        next_dir.row = r
        next_dir.col = c
        next_pos.row = Sapiens.location.row + next_dir.row
        next_pos.col = Sapiens.location.col + next_dir.col
    if Sapiens.field.getObjectAt(next_pos):
        if Sapiens.colour == 'red' and Sapiens.field._field[next_pos.row][
            next_pos.col].colour == 'slate blue' and random.random() <= Virus.INFECTION_RATE:
            Sapiens.field._field[next_pos.row][next_pos.col].colour = 'red'
            Sapiens.field._field[next_pos.row][next_pos.col].r_or_d = Stats.step + Virus.RECOVERY_TIME
            Sapiens.numberInfected = Sapiens.numberInfected + 1
            Stats.I = Stats.I + 1
            Stats.S = Stats.S - 1
        r = Sapiens.field._field[next_pos.row][next_pos.col].velocity.row
        c = Sapiens.field._field[next_pos.row][next_pos.col].velocity.col
        Sapiens.field._field[next_pos.row][next_pos.col].velocity.row = next_dir.row
        Sapiens.field._field[next_pos.row][next_pos.col].velocity.col = next_dir.col
        next_dir.row = r
        next_dir.col = c
        next_pos.row = Sapiens.location.row + next_dir.row
        next_pos.col = Sapiens.location.col + next_dir.col
    if Sapiens.field.getObjectAt(next_pos):
        if Sapiens.colour == 'red' and Sapiens.field._field[next_pos.row][
            next_pos.col].colour == 'slate blue' and random.random() <= Virus.INFECTION_RATE:
            Sapiens.field._field[next_pos.row][next_pos.col].colour = 'red'
            Sapiens.field._field[next_pos.row][next_pos.col].r_or_d = Stats.step + Virus.RECOVERY_TIME
            Sapiens.numberInfected = Sapiens.numberInfected + 1
            Stats.I = Stats.I + 1
            Stats.S = Stats.S - 1
        r = Sapiens.field._field[next_pos.row][next_pos.col].velocity.row
        c = Sapiens.field._field[next_pos.row][next_pos.col].velocity.col
        Sapiens.field._field[next_pos.row][next_pos.col].velocity.row = next_dir.row
        Sapiens.field._field[next_pos.row][next_pos.col].velocity.col = next_dir.col
        next_dir.row = r
        next_dir.col = c
        next_pos.row = Sapiens.location.row + next_dir.row
        next_pos.col = Sapiens.location.col + next_dir.col


    Sapiens.velocity.row = next_dir.row
    Sapiens.velocity.col = next_dir.col
    if Sapiens.field.getObjectAt(
            next_pos) or next_pos.col < 0 or next_pos.col >= Sapiens.field.size or next_pos.row < 0 or next_pos.row >= Sapiens.field.size:
        return Sapiens.location
    return next_pos
