from decimal import Decimal, getcontext

def bisection (a,b):

    def func(x):
        return x**2 - 4
    
    getcontext().prec = (20)
    a, b = Decimal(1), Decimal(3)
    tolerance = Decimal('1e-20')
    while b - a > tolerance:
        c = (a+b) / 2
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return c


    

