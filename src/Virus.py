"""Virus characteristics.

   These are absolutely arbitrary.
   :author: Peter Sander

"""
# the probability of passing the virus
#  upon contact between sapienses
INFECTION_RATE = 0.9

# the number of steps that a sapiens remains infected before
#  passing to the next state
RECOVERY_TIME = 60

# the probability of passing from infected to dead
# hence the probability of recovering is 1 - MORBIDITY_RATE
MORBIDITY_RATE = 0.5