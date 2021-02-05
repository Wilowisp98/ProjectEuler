# Which starting number, under one million, produces the longest chain?

# Comments Section:
# - Straight forward algorithm using a cache

def collatz(x):
    if x % 2 == 0:
        return x/2
    if x==1:
        return 1
    else:
        return 1 + 3*x

def problem14():
    cache = {}
    maxn = 0
    maxc = 0
    for i in range(2,1000001):
        number = i
        counter = 0
        while i != 1:
            if i in cache:
                counter += cache[i] 
                break
            else:
                i = collatz(i)
                counter += 1
        cache[number] = counter
        if counter > maxc:
            maxc = counter
            maxn = number
    return ("The biggest number is " +  str(maxn) + " with a chain of " + str(maxc))
