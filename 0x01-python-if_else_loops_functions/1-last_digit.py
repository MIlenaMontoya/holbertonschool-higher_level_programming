#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
        LastD = number % 10
else:
        LastD = number % -10
string1 = "Last digit of"

if LastD > 5:
        print("{:s} {:d} is {:d} and greater than 5".format(string1, number, LastD))
elif LastD == 0:
        print("{:s} {:d} is {:d} and is 0".format(string1, number, LastD))
else:
        string2 = "and is less than 6 and not 0"
        print("{:S} {:d} is {:d} {:s}".format(string1, number, LastD, string2))
