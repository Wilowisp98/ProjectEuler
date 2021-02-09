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
                

