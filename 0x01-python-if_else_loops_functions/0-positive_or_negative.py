#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# if the number is greater than 0: is positive
if number > 0:
    print("{} "'is positive'.format(number))
# if the number is 0: is zero
if number == 0:
    print("{} "'is zero'.format(number))
# if the number is less than 0: is negative
if number < 0:
    print("{} "'is negative'.format(number))
