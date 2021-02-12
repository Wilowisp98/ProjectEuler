# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Comments Section:
# - You don't really need to build the squares and then sum the diagonals,
# at first I simply worked on how the sum of each cycle works, a cycle
# is the sum of every corner on a square, so, the first one was 3 + 5 + 7 9,
# the second was 13 + 17 + 21 + 25 and so on... The difference between a cycle
# is +8, starting on 2, that is, 3 + (2+8) = 13, 13 + (2+8+8) = 31 ...
# Other thing is that the difference on each corner of the same square differs
# by +2 starting on 2, that is, 3 + 2 = 5, 5 + 2 = 7, 7 + 2 = 9.
# The first try was just around that.
# - The second try just looks cleaner, it's based on the fact that for each square
# the sum of it's corners is 4*(n**2) - 6*(n-1). The value of n needs to be odd.

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
        
    
