from decimal import Decimal, getcontext

def bisection (a,b):

    def func(x):
        return x**2 - 4
    
    getcontext().prec = 20
    a = Decimal(str(a))
    b = Decimal(str(b))
    tolerance = Decimal('1e-20')
    while b - a > tolerance:
        c = (a+b) / 2
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return c
print(bisection(1,3))


    

