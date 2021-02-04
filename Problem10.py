# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Comments Section:
# - Straight forward algorithm using the fact that (if A divibes B) that implies that (A <= sqrt(B)) 

import math as m

def isprime(x):
    for i in range(2,int(m.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def problem10():
    sum = 0
    for i in range(2,2000000):
        if isprime(i) is True:
            sum += i
    return sum    
