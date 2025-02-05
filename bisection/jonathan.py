import math
def bisection(xl,xr,sf):
    while (xr-xl) > (10**-sf):
        xm = (xl+xr)/2
        if math.tan(xm) - xm > 0:
            xr = xm
        elif math.tan(xm) - xm < 0:
            xl = xm
        print(xr,xl)
        print((xr-xl),(10**-sf))
    return round((xr+xl)/2,sf)

bisection(4,5,15)
print("hello world")