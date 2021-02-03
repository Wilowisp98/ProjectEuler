# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Comments Section:
# - The LCM (Lowest Common Multiple) of two numbers is given by LCM(X,Y) = (X * Y) // GCD(X,Y) where
# GCD means Greatest Common Divisor.
# - It can be done easily by hand;
#   - 19 = 19
#   - 18 = 2 * 3^2
#   - 17 = 17
#   - 16 = 2^4
#   - 15 = 3 * 5
#   - 14 = 2 * 7
#   - 13 = 13
#   - 11 = 11
#   - ...
#   - So, LCM = 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232 792 560

from math import gcd

def problem5():
    LCM = 1
    for i in range(1, 21):
        LCM *= i // gcd(LCM, i)
    return LCM
    
