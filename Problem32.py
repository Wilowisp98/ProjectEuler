from math import sqrt

def problem32():
    nums = set()
    for i in range(1, 10000):
        for k in range(2, int(sqrt(i)) + 1):
            if i % k == 0:
                pandi = str(i) + str(k) + str(i//k)
                if ordstr(pandi) == "123456789":
                    nums.add(i)
    return sum(nums)

def ordstr(instr):
    list = []
    outstr = ""
    for i in instr:
        list.append(i)
    list.sort()
    for i in range(len(list)):
       outstr += str(list[i])
    return outstr
    
        
