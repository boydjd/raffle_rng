#!/usr/bin/env python
# save as cgi-bin/index.py
# Python 2.7
import cgi
import cgitb; cgitb.enable()
import random
import platform
import math

form = cgi.FieldStorage()
html = """
<html>
<head>
</head>
<body>
<form action="index.py" name="myform" method="GET">
            Enter total slots:  <input type="text" name="slots"><br />
                    Enter seed: <input type="text" name="seed"><br />
                            <input type="submit" value="submit">
                        </form>
                        </body>
                        </html>
"""
try:
    slots = int(form['slots'].value)

    # the seed you're testing
    seed = form['seed'].value

    # This sets the seed that python uses to
    # generate the random number
    # random.seed(seed)
    rnd = random.Random(int(seed, 16))

    # This is our actual random number
    # Minimum is always 0
    # Maximum is one million times number of slots minus one
    # which will give an even distribution chance
    min = 0
    max = (slots * math.pow(10, 6)) - 1
    # big_result = random.randint(min, max)
    big_result = rnd.randint(min, max)

    # The winning number is the big random number
    # modulus the number of slots plus one
    # Modulus would normally return 0 to SLOTS-1
    # but the + 1 makes it return 1 to SLOTS
    # which is what we want
    winner = big_result % slots + 1

    response = """
    The winner is {}
    Seed: {}
    Seed (long): {}
    Random Number: {}
    Minimum: {}
    Maximum: {}
    Modulus: {}
    Python: {}
    """.format(winner, seed, int(seed, 16),
            big_result, min, max, slots,
                    platform.python_version())

    print(response)
except KeyError:
    print html

