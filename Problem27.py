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
            
    
