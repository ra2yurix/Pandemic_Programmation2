from random import randint, Random


class Randomizer(object):
    """Provide control over the randomization of the simulation.

    :author: David J. Barnes and Michael Kolling
    :author: Peter Sander
    :author: ZHENG Yannan
    """
    #  The default seed for control of randomization.
    _SEED = 1111
    #  A shared Random object, if required.
    _rand = Random(_SEED)
    #  Determine whether a shared random generator is to be provided.
    _useShared = False

    @classmethod
    def getRandom(cls):
        """Provide a random generator.
        :return: A random object.
        """
        if cls._useShared:
            return cls._rand
        else:
            return Random()

    @classmethod
    def reset(cls):
        """Reset the randomization. This will have no effect if randomization is not
        through a shared Random generator.
        """
        if cls._useShared:
            cls._rand.seed(cls._SEED)
