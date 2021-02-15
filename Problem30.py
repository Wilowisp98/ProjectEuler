# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Comments Section:
# - Used 6*(9**5) as the upper bound because 6*(9**5) is the highest number made of the sum of six fifth power numbers

def problem30():
    return sum([x for x in range(2,6*(9**5)) if x == sum([int(y)**5 for y in str(x)])])
                
