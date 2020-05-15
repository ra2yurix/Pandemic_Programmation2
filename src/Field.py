from random import shuffle
import Particle
from Position import Position
from Position import Direction
from Randomizer import Randomizer


class Field():
    """Represent a square grid of field positions.

    Each position is able to store a single particle.
    :author: David J. Barnes and Michael Kolling
    :author: Peter Sander
    """
    _rand = Randomizer.getRandom().random

    def __init__(self, size):
        self.size = size
        self.clear()

    def clear(self, position: Position = None) -> None:
        """Empty the field or clear the given position.

        :position: The position to clear, or None to empty the field.
        """
        if position is None:
            self._field = [[None]*self.size for i in range(self.size)]
        else:
            self._field[position.row][position.col] = None

    def place(self, particle: Particle) -> None:
        """Place a particle at the given position.

        If there is already a particle at the position it will be overwritten.
        """
        position = particle.position
        self._field[position.row][position.col] = particle

    def getObjectAt(self, position: Position) -> Particle:
        """Return the particle at the given position, if any.

        :position: The position.
        :return: The particle at the given position, or None if there is none.
        """
        return self._field[position.row][position.col]

    def freeAdjacentPosition(self, particle: Particle, radius: int) -> Position:
        """Try to find a free position that is adjacent to the given particle's
        position.

        The returned position will be within the bounds of the field.
        :return: A valid position within the grid area, otherwise None.
        """
        next_pos = Position(particle.position.row + particle.direction.row,
                            particle.position.col + particle.direction.col)
        next_dir = Direction(particle.direction.row, particle.direction.col)

        if next_pos.col <= 0 or next_pos.col >= self.size - 1:
            next_pos.col = particle.position.col - next_dir.col
            next_dir.col = - next_dir.col
        if next_pos.row <= 0 or next_pos.row >= self.size - 1:
            next_pos.row = particle.position.row - next_dir.row
            next_dir.row = -next_dir.row

        if self.getObjectAt(next_pos):
            r = self._field[next_pos.row][next_pos.col].direction.row
            c = self._field[next_pos.row][next_pos.col].direction.col
            self._field[next_pos.row][next_pos.col].direction.row = next_dir.row
            self._field[next_pos.row][next_pos.col].direction.col = next_dir.col
            next_dir.row = r
            next_dir.col = c
            next_pos.row = particle.position.row + next_dir.row
            next_pos.col = particle.position.col + next_dir.col
        if self.getObjectAt(next_pos):
            r = self._field[next_pos.row][next_pos.col].direction.row
            c = self._field[next_pos.row][next_pos.col].direction.col
            self._field[next_pos.row][next_pos.col].direction.row = next_dir.row
            self._field[next_pos.row][next_pos.col].direction.col = next_dir.col
            next_dir.row = r
            next_dir.col = c
            next_pos.row = particle.position.row + next_dir.row
            next_pos.col = particle.position.col + next_dir.col
        if self.getObjectAt(next_pos):
            r = self._field[next_pos.row][next_pos.col].direction.row
            c = self._field[next_pos.row][next_pos.col].direction.col
            self._field[next_pos.row][next_pos.col].direction.row = next_dir.row
            self._field[next_pos.row][next_pos.col].direction.col = next_dir.col
            next_dir.row = r
            next_dir.col = c
            next_pos.row = particle.position.row + next_dir.row
            next_pos.col = particle.position.col + next_dir.col
        if self.getObjectAt(next_pos):
            r = self._field[next_pos.row][next_pos.col].direction.row
            c = self._field[next_pos.row][next_pos.col].direction.col
            self._field[next_pos.row][next_pos.col].direction.row = next_dir.row
            self._field[next_pos.row][next_pos.col].direction.col = next_dir.col
            next_dir.row = r
            next_dir.col = c
            next_pos.row = particle.position.row + next_dir.row
            next_pos.col = particle.position.col + next_dir.col
        # if particle.position.row + 2 * particle.direction.row >= 0 and particle.position.row \
        #         + 2 * particle.direction.row < self.size and particle.position.col \
        #         + 2 * particle.direction.col >= 0 and particle.position.col + 2 * particle.direction.col < self.size:
        #     next_pos_2 = Position(particle.position.row + 2 * particle.direction.row,
        #                           particle.position.col + particle.direction.col)
        #     next_pos_3 = Position(particle.position.row + particle.direction.row,
        #                           particle.position.col + 2 * particle.direction.col)
        #     next_pos_4 = Position(particle.position.row + 2 * particle.direction.row,
        #                           particle.position.col + 2 * particle.direction.col)
        #     if self.getObjectAt(next_pos_2):
        #         r = self._field[next_pos_2.row][next_pos_2.col].direction.row
        #         c = self._field[next_pos_2.row][next_pos_2.col].direction.col
        #         self._field[next_pos_2.row][next_pos_2.col].direction.row = next_dir.row
        #         self._field[next_pos_2.row][next_pos_2.col].direction.col = next_dir.col
        #         next_dir.row = r
        #         next_dir.col = c
        #         next_pos.row = particle.position.row + next_dir.row
        #         next_pos.col = particle.position.col + next_dir.col
        #     if self.getObjectAt(next_pos_3):
        #         r = self._field[next_pos_3.row][next_pos_3.col].direction.row
        #         c = self._field[next_pos_3.row][next_pos_3.col].direction.col
        #         self._field[next_pos_3.row][next_pos_3.col].direction.row = next_dir.row
        #         self._field[next_pos_3.row][next_pos_3.col].direction.col = next_dir.col
        #         next_dir.row = r
        #         next_dir.col = c
        #         next_pos.row = particle.position.row + next_dir.row
        #         next_pos.col = particle.position.col + next_dir.col
        #     if self.getObjectAt(next_pos_4):
        #         r = self._field[next_pos_4.row][next_pos_4.col].direction.row
        #         c = self._field[next_pos_4.row][next_pos_4.col].direction.col
        #         self._field[next_pos_4.row][next_pos_4.col].direction.row = next_dir.row
        #         self._field[next_pos_4.row][next_pos_4.col].direction.col = next_dir.col
        #         next_dir.row = r
        #         next_dir.col = c
        #         next_pos.row = particle.position.row + next_dir.row
        #         next_pos.col = particle.position.col + next_dir.col
        #
        # if next_pos.col < 0 or next_pos.col >= self.size:
        #     next_pos.col = particle.position.col - next_dir.col
        #     next_dir.col = - next_dir.col
        # if next_pos.row <= 0 or next_pos.row >= self.size - 1:
        #     next_pos.row = particle.position.row - next_dir.row
        #     next_dir.row = -next_dir.row
        # if self.getObjectAt(next_pos):
        #     r = self._field[next_pos.row][next_pos.col].direction.row
        #     c = self._field[next_pos.row][next_pos.col].direction.col
        #     self._field[next_pos.row][next_pos.col].direction.row = next_dir.row
        #     self._field[next_pos.row][next_pos.col].direction.col = next_dir.col
        #     next_dir.row = r
        #     next_dir.col = c
        #     next_pos.row = particle.position.row + next_dir.row
        #     next_pos.col = particle.position.col + next_dir.col
        #
        # if next_pos.col < 0 or next_pos.col >= self.size:
        #     next_pos.col = particle.position.col - next_dir.col
        #     next_dir.col = - next_dir.col
        # if next_pos.row <= 0 or next_pos.row >= self.size - 1:
        #     next_pos.row = particle.position.row - next_dir.row
        #     next_dir.row = -next_dir.row
        # if self.getObjectAt(next_pos):
        #     r = self._field[next_pos.row][next_pos.col].direction.row
        #     c = self._field[next_pos.row][next_pos.col].direction.col
        #     self._field[next_pos.row][next_pos.col].direction.row = next_dir.row
        #     self._field[next_pos.row][next_pos.col].direction.col = next_dir.col
        #     next_dir.row = r
        #     next_dir.col = c
        #     next_pos.row = particle.position.row + next_dir.row
        #     next_pos.col = particle.position.col + next_dir.col

        particle.direction.row = next_dir.row
        particle.direction.col = next_dir.col
        if self.getObjectAt(
                next_pos) or next_pos.col < 0 or next_pos.col >= self.size or next_pos.row < 0 or next_pos.row >= self.size:
            return particle.position
        return next_pos

    def _adjacentPositions(self, particle: Particle, radius) -> list:
        """Return a shuffled list of positions adjacent to the given one.

        The list will not include the particle position itself.
        All positions lie within the grid.
        :radius: Radius of adjacent locations.
        :return: A list of positions adjacent to the particle.
        """
        position = particle.position
        positions = []
        if position is not None:
            row = position.row
            col = position.col
            for roffset in range(-radius, radius + 1):
                nextRow = row + roffset
                if 0 <= nextRow < self.size:
                    for coffset in range(-radius, radius + 1):
                        nextCol = col + coffset
                        # excludes particle position
                        if 0 <= nextCol < self.size \
                                and (roffset != 0 or coffset != 0):
                            positions.append(Position(nextRow, nextCol))
            # randomize position order.
            shuffle(positions, Field._rand)
        return positions
