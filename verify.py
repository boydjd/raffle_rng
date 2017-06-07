#!/usr/bin/python

# Once you enter the seed and number of slots
# you should be able to run this script repeatedly
# and get he same result every time you run it
#
# Make sure to also be running the same version of
# Python, or else you might get a different result

import random
import platform
import math

# Put the number of slots here
# Used as a modulus and max calculation
# of random number
slots = 30

# the seed you're testing
seed = 'PASTE_SEED_HERE'

# This sets the seed that python uses to 
# generate the random number
random.seed(seed)

# This is our actual random number
# Minimum is always 0
# Maximum is one million times number of slots minus one
# which will give an even distribution chance
min = 0
max = (slots * math.pow(10, 6)) - 1
big_result = random.randint(min, max)

# The winning number is the big random number 
# modulus the number of slots plus one
# Modulus would normally return 0 to SLOTS-1
# but the + 1 makes it return 1 to SLOTS
# which is what we want
winner = big_result % slots + 1

response = """
The winner is {}
Seed: {}
Random Number: {}
Minimum: {}
Maximum: {}
Modulus: {}
Python: {}
""".format(winner, seed, 
        big_result, min, max, slots, 
        platform.python_version())

print(response)
