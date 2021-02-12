# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

# Comments Section:
# - On isprime is just a way of checking if a number is prime or not, and, if it is, it's added on the cache.
# - On problem27, you can tell that, if n=0, the quadratic is equal to b, and for n=0 to be a prime, b needs to be a prime,
# so we only need to check the values where b is prime.
# For a, if n = 1, we have p = 1 + b + a, where p needs to be prime, if b is prime, b + 1 is even because b can be written as
# 2*K + 1 and 2*K + 1 + 1 = 2*K + 2 that is even, and, for p to have a chance of being prime, a has to be odd.

from math import sqrt

primescache = {}

def isprime(n):
    if n in primescache:
        return True
    if n < 0:
        return False
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    primescache[n] = 1
    return True

def problem27():
    max = 0
    maxa = 0
    maxb = 0
    for b in [x for x in range(3,999) if isprime(x)]:
        for a in range(-999,1000,2):
            n = 0
            cons = 0
            while True:
                value = (n**2) + (a * n) + b
                if isprime(value) is False:
                    break
                cons += 1
                n += 1
            if cons > max:
                max = cons
                maxa = a
                maxb = b
    return maxa*maxb
            
    
