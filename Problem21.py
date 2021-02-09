# Evaluate the sum of all the amicable numbers under 10000.

# Comments Section:
# - Straight forward algorithm

def divisorssum(n):
    sum = 0
    for i in range(1,(int(n/2))+1):
        if n % i == 0:
            sum += i
    return sum
        
def problem21():
    sum = 0
    numbers = []
    for i in range(1,10000):
        if i not in numbers:
            if (divisorssum(divisorssum(i)) == i) and (divisorssum(i) != i) :
                sum += divisorssum(i) + i
                numbers.append(divisorssum(i))
                numbers.append(i)
    return sum
