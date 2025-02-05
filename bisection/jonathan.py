import math
from decimal import Decimal, getcontext
def bisection(xl,xr,sf):
    getcontext().prec = sf+20
    xl = Decimal(xl)
    xr = Decimal(xr)
    while (xr-xl) > (10**-sf):
        xm = Decimal((xl+xr)/2)
        if Decimal(math.tan(xm)) - xm > 0:
            xr = xm
        elif Decimal(math.tan(xm)) - xm < 0:
            xl = xm
    return round((xr+xl)/2,sf)

f = bisection(4,5,50)
print(f)    

