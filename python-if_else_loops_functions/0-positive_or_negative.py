#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive".format(number))
elif number == 0:
    print("%s is zero" % number)
elif number < 0:
    print("%s is negative" % number)
