# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Comments Section:
# - This is a combinatorial problem. To get from one corner to the other we have to move 40 times,
# 20 times right and 20 times down, however, if we decide where we are going to walk down, or right,
# it's is already decided where we are going to walk right, or down.
# For example, let's do it on a 2x2 grid, where we have to walk 4 times, 2 times down and 2 times right:
#   - (R,R,_,_); (R,_,R,_); (R,_,_,R); (_,R,R,_); (_,R,_,R); (_,_,R,R)
#   - So, as you can tell, all we have to do is C(4,2), in 4 spots, decide where to put 2Rs.

def problem15():
    return int(factorial(40) / (factorial(20)**2))

def factorial(x):
    value = 1
    for i in range(1,x+1):
        value *= i
    return value
