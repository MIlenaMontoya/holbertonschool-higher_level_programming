#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
        ld = number % 10
else:
        ld = number % -10
st1 = "Last digit of "
if ld > 5:
        print("{}{} is {} and greater than 5".format(st1, number, ld))
elif ld == 0:
        print("{}{} is {} and is 0".format(st1, number, ld))
else:
        st2 = "and is less than 6 and not 0"
        print("{}{} is {} {}".format(st1, number, ld, st2))
