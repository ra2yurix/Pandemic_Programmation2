S = 0
I = 0
R = 0
D = 0
step = 0
I0 = 0

def isViable() -> bool:
    """Determine whether the simulation is still viable, ie, should it
    continue to run.

    When no infected sapiens are left, the simulation stops.
    :return: True if there are any infected sapiens left.
    """
    if I != 0:
        return True
    return False


def calculateR(sapienses: list) -> float:
    """Calculates the current effective reproduction number.

    :param sapienses:
    :return: R, the effective reproduction number.
    """
    r = 0
    for i in sapienses:
        r = r + i.numberInfected
    # r=r/I
    # r = r*S/(S+R+D)
    return r
