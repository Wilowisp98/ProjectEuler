# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Comments Section:
# - It was just based on the fact that if (A divibes B) that implies that (A <= sqrt(B)) 

import math as m

def isprime(x):
    for i in range(2,int(m.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
        
def problem3():
    n = 600851475143
    t = int(m.sqrt(600851475143))
    for i in range(t, 1, -1):
        if (n % i == 0) and (isprime(i) == True):
            return i
