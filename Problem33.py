from math import gcd

def problem33():
    num = 1
    den = 1
    for i in range(10,100):
        for j in range(1,10):
            a = i // 10
            b = i % 10
            c = j
            f = j
            if (-9*b*c) + 10*c*a - b*a == 0 and b/c < 1:
                num *= b
                den *= c
            if 9*a*f + f*b - a*b*10 == 0 and a/f < 1:
                num *= a
                den *= f
    return den//(gcd(num,den))
                
               
            
            
