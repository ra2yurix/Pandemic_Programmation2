from random import shuffle
import Sapiens
from Location import Location
from Location import Velocity
from Randomizer import Randomizer


class Field():
    """Represent a square grid of field locations.

    Each location is able to store a single Sapiens.
    :author: David J. Barnes and Michael Kolling
    :author: Peter Sander
    """
    _rand = Randomizer.getRandom().random

    def __init__(self, size):
        self.size = size
        self.clear()

    def clear(self, location: Location = None) -> None:
        """Empty the field or clear the given location.

        :location: The location to clear, or None to empty the field.
        """
        if location is None:
            self._field = [[None]*self.size for i in range(self.size)]
        else:
            self._field[location.row][location.col] = None

    def place(self, Sapiens: Sapiens) -> None:
        """Place a Sapiens at the given location.

        If there is already a Sapiens at the location it will be overwritten.
        """
        location = Sapiens.location
        self._field[location.row][location.col] = Sapiens

    def getObjectAt(self, location: Location) -> Sapiens:
        """Return the Sapiens at the given location, if any.

        :location: The location.
        :return: The Sapiens at the given location, or None if there is none.
        """
        return self._field[location.row][location.col]

    def freeAdjacentLocation(self, Sapiens: Sapiens, radius: int) -> Location:
        """Try to find a free location that is adjacent to the given Sapiens's
        location.

        The returned location will be within the bounds of the field.
        :return: A valid location within the grid area, otherwise None.
        """
        next_pos = Location(Sapiens.location.row + Sapiens.velocity.row,
                            Sapiens.location.col + Sapiens.velocity.col)
        next_dir = Velocity(Sapiens.velocity.row, Sapiens.velocity.col)

        if next_pos.col <= 0 or next_pos.col >= self.size - 1:
            next_pos.col = Sapiens.location.col - next_dir.col
            next_dir.col = - next_dir.col
        if next_pos.row <= 0 or next_pos.row >= self.size - 1:
            next_pos.row = Sapiens.location.row - next_dir.row
            next_dir.row = -next_dir.row

        if self.getObjectAt(next_pos):
            r = self._field[next_pos.row][next_pos.col].velocity.row
            c = self._field[next_pos.row][next_pos.col].velocity.col
            self._field[next_pos.row][next_pos.col].velocity.row = next_dir.row
            self._field[next_pos.row][next_pos.col].velocity.col = next_dir.col
            next_dir.row = r
            next_dir.col = c
            next_pos.row = Sapiens.location.row + next_dir.row
            next_pos.col = Sapiens.location.col + next_dir.col
        if self.getObjectAt(next_pos):
            r = self._field[next_pos.row][next_pos.col].velocity.row
            c = self._field[next_pos.row][next_pos.col].velocity.col
            self._field[next_pos.row][next_pos.col].velocity.row = next_dir.row
            self._field[next_pos.row][next_pos.col].velocity.col = next_dir.col
            next_dir.row = r
            next_dir.col = c
            next_pos.row = Sapiens.location.row + next_dir.row
            next_pos.col = Sapiens.location.col + next_dir.col
        if self.getObjectAt(next_pos):
            r = self._field[next_pos.row][next_pos.col].velocity.row
            c = self._field[next_pos.row][next_pos.col].velocity.col
            self._field[next_pos.row][next_pos.col].velocity.row = next_dir.row
            self._field[next_pos.row][next_pos.col].velocity.col = next_dir.col
            next_dir.row = r
            next_dir.col = c
            next_pos.row = Sapiens.location.row + next_dir.row
            next_pos.col = Sapiens.location.col + next_dir.col
        if self.getObjectAt(next_pos):
            r = self._field[next_pos.row][next_pos.col].velocity.row
            c = self._field[next_pos.row][next_pos.col].velocity.col
            self._field[next_pos.row][next_pos.col].velocity.row = next_dir.row
            self._field[next_pos.row][next_pos.col].velocity.col = next_dir.col
            next_dir.row = r
            next_dir.col = c
            next_pos.row = Sapiens.location.row + next_dir.row
            next_pos.col = Sapiens.location.col + next_dir.col
        # if Sapiens.location.row + 2 * Sapiens.velocity.row >= 0 and Sapiens.location.row \
        #         + 2 * Sapiens.velocity.row < self.size and Sapiens.location.col \
        #         + 2 * Sapiens.velocity.col >= 0 and Sapiens.location.col + 2 * Sapiens.velocity.col < self.size:
        #     next_pos_2 = Location(Sapiens.location.row + 2 * Sapiens.velocity.row,
        #                           Sapiens.location.col + Sapiens.velocity.col)
        #     next_pos_3 = Location(Sapiens.location.row + Sapiens.velocity.row,
        #                           Sapiens.location.col + 2 * Sapiens.velocity.col)
        #     next_pos_4 = Location(Sapiens.location.row + 2 * Sapiens.velocity.row,
        #                           Sapiens.location.col + 2 * Sapiens.velocity.col)
        #     if self.getObjectAt(next_pos_2):
        #         r = self._field[next_pos_2.row][next_pos_2.col].velocity.row
        #         c = self._field[next_pos_2.row][next_pos_2.col].velocity.col
        #         self._field[next_pos_2.row][next_pos_2.col].velocity.row = next_dir.row
        #         self._field[next_pos_2.row][next_pos_2.col].velocity.col = next_dir.col
        #         next_dir.row = r
        #         next_dir.col = c
        #         next_pos.row = Sapiens.location.row + next_dir.row
        #         next_pos.col = Sapiens.location.col + next_dir.col
        #     if self.getObjectAt(next_pos_3):
        #         r = self._field[next_pos_3.row][next_pos_3.col].velocity.row
        #         c = self._field[next_pos_3.row][next_pos_3.col].velocity.col
        #         self._field[next_pos_3.row][next_pos_3.col].velocity.row = next_dir.row
        #         self._field[next_pos_3.row][next_pos_3.col].velocity.col = next_dir.col
        #         next_dir.row = r
        #         next_dir.col = c
        #         next_pos.row = Sapiens.location.row + next_dir.row
        #         next_pos.col = Sapiens.location.col + next_dir.col
        #     if self.getObjectAt(next_pos_4):
        #         r = self._field[next_pos_4.row][next_pos_4.col].velocity.row
        #         c = self._field[next_pos_4.row][next_pos_4.col].velocity.col
        #         self._field[next_pos_4.row][next_pos_4.col].velocity.row = next_dir.row
        #         self._field[next_pos_4.row][next_pos_4.col].velocity.col = next_dir.col
        #         next_dir.row = r
        #         next_dir.col = c
        #         next_pos.row = Sapiens.location.row + next_dir.row
        #         next_pos.col = Sapiens.location.col + next_dir.col
        #
        # if next_pos.col < 0 or next_pos.col >= self.size:
        #     next_pos.col = Sapiens.location.col - next_dir.col
        #     next_dir.col = - next_dir.col
        # if next_pos.row <= 0 or next_pos.row >= self.size - 1:
        #     next_pos.row = Sapiens.location.row - next_dir.row
        #     next_dir.row = -next_dir.row
        # if self.getObjectAt(next_pos):
        #     r = self._field[next_pos.row][next_pos.col].velocity.row
        #     c = self._field[next_pos.row][next_pos.col].velocity.col
        #     self._field[next_pos.row][next_pos.col].velocity.row = next_dir.row
        #     self._field[next_pos.row][next_pos.col].velocity.col = next_dir.col
        #     next_dir.row = r
        #     next_dir.col = c
        #     next_pos.row = Sapiens.location.row + next_dir.row
        #     next_pos.col = Sapiens.location.col + next_dir.col
        #
        # if next_pos.col < 0 or next_pos.col >= self.size:
        #     next_pos.col = Sapiens.location.col - next_dir.col
        #     next_dir.col = - next_dir.col
        # if next_pos.row <= 0 or next_pos.row >= self.size - 1:
        #     next_pos.row = Sapiens.location.row - next_dir.row
        #     next_dir.row = -next_dir.row
        # if self.getObjectAt(next_pos):
        #     r = self._field[next_pos.row][next_pos.col].velocity.row
        #     c = self._field[next_pos.row][next_pos.col].velocity.col
        #     self._field[next_pos.row][next_pos.col].velocity.row = next_dir.row
        #     self._field[next_pos.row][next_pos.col].velocity.col = next_dir.col
        #     next_dir.row = r
        #     next_dir.col = c
        #     next_pos.row = Sapiens.location.row + next_dir.row
        #     next_pos.col = Sapiens.location.col + next_dir.col

        Sapiens.velocity.row = next_dir.row
        Sapiens.velocity.col = next_dir.col
        if self.getObjectAt(
                next_pos) or next_pos.col < 0 or next_pos.col >= self.size or next_pos.row < 0 or next_pos.row >= self.size:
            return Sapiens.location
        return next_pos

    def _adjacentLocations(self, Sapiens: Sapiens, radius) -> list:
        """Return a shuffled list of locations adjacent to the given one.

        The list will not include the Sapiens location itself.
        All locations lie within the grid.
        :radius: Radius of adjacent locations.
        :return: A list of locations adjacent to the Sapiens.
        """
        location = Sapiens.location
        locations = []
        if location is not None:
            row = location.row
            col = location.col
            for roffset in range(-radius, radius + 1):
                nextRow = row + roffset
                if 0 <= nextRow < self.size:
                    for coffset in range(-radius, radius + 1):
                        nextCol = col + coffset
                        # excludes Sapiens location
                        if 0 <= nextCol < self.size \
                                and (roffset != 0 or coffset != 0):
                            locations.append(Location(nextRow, nextCol))
            # randomize location order.
            shuffle(locations, Field._rand)
        return locations
