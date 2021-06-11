# @author: ANISHK YADAV

"""
TASK
Given an integer, n , perform the following conditional actions:

If n is odd, print "Weird"
If n is even and in the inclusive range of 2 to 5, print "Not Weird"
If n is even and in the inclusive range of 6 to 20, print "Weird"
If n is even and greater than 20, print "Not Weird" """

# CODE:

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())


def weird_or_not():
    if (n % 2) != 0:
        print("Weird")
    elif (n % 2) == 0 in range(2, 5):
        print("Not Weird")
    elif (n % 2) == 0 in range(6, 20):
        print("Weird")
    else:
        print("Not Weird")


weird_or_not()
