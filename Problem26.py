# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# Comments Section:
# - This exercice can be easily done by hand.
# Gonna make 1 by hand so you can understand what's going on:
# 7*1 + 3 = 10
# 7*4 + 2 = 3*10
# 7*2 + 6 = 2*10
# 7*8 + 4 = 6*10
# 7*5 + 5 = 4*10
# 7*7 + 1 = 5*10
# And then it repeats, so, 1/7 = 0.(142857)

def cyclelen(n):
    l = 0
    history = {}
    dividend = 10
    while True:
        if dividend in history:
            return l
        else:
            history[dividend] = dividend//n
            dividend = (dividend % n)*10
            l += 1
        
def problem26():
    num = 0
    maxlen = 0
    for i in range(1,1000):
        leni = cyclelen(i)
        if leni > maxlen:
            maxlen = leni
            num = i
    return num
