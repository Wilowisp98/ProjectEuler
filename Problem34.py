from math import factorial

def problem34():
    sum = 0
    for i in range(3,10000000):
        if checker(i) is True:
            sum += i
    return sum

def checker(n):
    sum = 0
    for i in str(n):
        sum += factorial(int(i))
    if n == sum:
        return True
    return False
