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
