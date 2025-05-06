import math
from decimal import Decimal, getcontext
import random

def function(x):
    return x**2 - 16 #Decimal(math.tan(x)) - x

def bisection(xl,xr,sf):

    getcontext().prec = sf+20
    xl = Decimal(xl)
    xr = Decimal(xr)

    while (xr-xl) > (10**-sf):
        xm = Decimal((xl+xr)/2)

        if function(xm)*function(xl) > 0:
            xl = xm
        else:
            xr = xm
        #print(function(xm),xm)
    return round((xr+xl)/2,sf)

def to_s_points(x):
    #compare differences from 0 and whichever gets closer is yippee ?

    if function(x) == 0: 
        return [x,x] #return literally the only point lmao (since we found the root)
    
    #init variables
    fx_init = function(x)
    x_sign = fx_init > 0
    print(x_sign)

    #checking ascent/descent, if it alr changes sign then 
    
    


    return [x,fx_init] #return original and fixed maybe the thing would only need one input now :D



#x = bisection(-300,300000,50)
#print(x,function(x))
#print(function(-3),function(30))    
print(to_s_points(3))

#current objective is to just find one root, cuz idk
