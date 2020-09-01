#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
        LastD = number % 10
else:
        LastD = number % -10
string1 = "Last digit of"
if LastD > 5:
        print("{} {} is {} and greater than 5".format(string1, number, LastD))
elif LastD == 0:
        print("{} {} is {} and is 0".format(string1, number, LastD))
else:
        string2 = "and is less than 6 and not 0"
        print("{} {} is {} {}".format(string1, number, LastD, string2))
