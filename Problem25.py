fibonaccicache = { 1 : 1, 2 : 1 }

def fibonacci(n):
    if n-1 in fibonaccicache:
        return fibonaccicache[n-1] + fibonaccicache[n-2]
    else:
        fibonaccicache[n-1] = fibonacci(n-1)
        return fibonaccicache[n-1] + fibonaccicache[n-2]

def problem25():
    n = 2
    fib = 1
    while len(str(fib)) < 1000:
        n += 1
        fib = fibonacci(n)
    return n
        
