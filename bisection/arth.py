import math
from decimal import Decimal, getcontext



getcontext().prec = (
    22  
) # sets the decimal to 22 dp


def function(x):
    return (
        Decimal(math.tan(float(x))) - x
    )  


a, b = Decimal(1), Decimal(3)  
tolerance = 0.00000000000000000001  # defines how small the root should be


while b - a > tolerance:  # continues until the difference is less than the tolerance
    c = (a + b) / 2  # calculates the midpoint
    if function(c) * function(a) < 0:  # checks where the root lies
        b = c  # if this, the root lies between a and c
    else:
        a = c  # if this the root lies between b and c

print(c)
