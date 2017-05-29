#!/usr/bin/python

# Once you enter the seed and number of slots
# you should be able to run this script repeatedly
# and get he same result every time you run it
#
# Make sure to also be running the same version of
# Python, or else you'll likely get a different result

import random
import platform

# Put the number of slots here
# Used as a modulus and max calculation
# of random number
slots = 3500

# the seed you're testing
seed = 'c939b0f9103d5c656736eb4298040b7ad25f2d6c'

# This sets the seed that python uses to 
# generate the random number
random.seed(seed)

# This is our actual random number
# Minimum is always 1
# Maximum is one million times number of slots
# which will give an even distribution chance
big_result = random.randint(1, slots * 1000000)

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
Modulus (slots): {}
Python: {}
""".format(winner, seed, 
        big_result, slots, 
        platform.python_version())

print(response)
