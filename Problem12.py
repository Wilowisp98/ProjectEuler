# What is the value of the first triangle number to have over five hundred divisors?

# Comments Section:
# - Straight forward algorithm but reducing the number of tests using factor pairs

from math import sqrt

def counter(n):
    counter = 0
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            counter += 1
    if sqrt(n)**2 == n:
        return counter*2 - 1
    else:
        return counter*2

def problem12():
    n = 0
    while True:
        n += 1
        if counter(((n+1)*n)/2) > 500:
            return int(((n+1)*n)/2)

        

    
        
    
