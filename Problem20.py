# Find the sum of the digits in the number 100!

# Comments Section:
# - Straight forward algorithm

def factorial(n):
    value = 1
    for i in range(2,n+1):
        value *= i
    return str(value)

def problem20():
    value = 0
    for i in factorial(100):
        value += int(i)
    return value
