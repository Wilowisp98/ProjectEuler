# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Comments Section:
# - Straight forward algorithm using that fact that 1+2+3+...+n-1+n = n*(n+1)/2

def abundants():
    abundlist = []
    for i in range(1,28123):
        value = 0
        for j in range(1,int(i/2) + 1):
            if i % j == 0:
                value += j
        if value > i:
            abundlist.append(i)
    return abundlist

def problem23():
    nums = set()
    abundlist = abundants()
    for i in range(len(abundlist)):
        for j in range(i, len(abundlist)):
            num = abundlist[i] + abundlist[j]
            if num <= 28123:
                nums.add(num)
    return (28123 * 28124) // 2 - sum(nums)
                

