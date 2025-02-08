import math
from decimal import Decimal, getcontext

# decimal makes it so that there will still be high precision and wtv number of decimal places


getcontext().prec = (
    22  # sets the decimal to 22 dp, extra 2 for some more added precision
)


# defines the function that will be going through the bisection
def function(x):
    return (
        Decimal(math.tan(float(x))) - x
    )  # have to put float and decimal if not no run idk


a, b = Decimal(1), Decimal(
    3
)  # these are the initial endpoints, using the decimal function so that it will be to 22 dp
tolerance = 0.00000000000000000001  # defines how small the root should be


while b - a > tolerance:  # continues until the difference is less than the tolerance
    c = (a + b) / 2  # calculates the midpoint
    if function(c) * function(a) < 0:  # checks where the root lies
        b = c  # if this, the root lies between a and c
    else:
        a = c  # if this the root lies between b and c

print(c)
