import math
from decimal import Decimal, getcontext
def bisection(xprel,xprer,sf):
    getcontext().prec = sf+20
    xl = Decimal(min(xprel,xprer))
    xr = Decimal(max(xprel,xprer))
    while (xr-xl) > Decimal(10**-sf):
        xm = Decimal((xl+xr)/2)
        if Decimal(math.tan(xm)) - xm > 0:
            xr = xm
        elif Decimal(math.tan(xm)) - xm < 0:
            xl = xm
    return round((xr+xl)/2,sf)

f = bisection(6,3,52)
print(f)   
