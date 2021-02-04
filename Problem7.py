# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Comments Section:
# - Straight forward algorithm.

import math as m

def isprime(x):
    for i in range(2,int(m.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def problem7():
    pcounter = 0
    i = 0
    while pcounter <= 10001:
        i += 1
        if isprime(i) is True:
            pcounter += 1
    return i
