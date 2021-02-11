
# First try

def problem28_1():
    starter = 3
    cyclemodifier = 2
    cyclecounter = 1
    sum = 0
    while starter <= 999001:
        sum += starter*4 + 12*cyclecounter
        cyclemodifier += 8
        starter += cyclemodifier
        cyclecounter += 1
    return sum + 1

# Second try thinking a bit more

def problem28_2():
    sum = 1
    n = 3
    while n <= 1001:
        sum += 4*(n**2) - 6*(n-1)
        n += 2
    return sum 
        
    
