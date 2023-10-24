import numpy as np
import math

#initial guess
xguess=1
diff=1e5
n=0
while abs(diff)>1e-12:
    x=(math.sin(4*xguess+3))**2/5
    diff=xguess-x
    xguess=x
    n+=1
    print(x)

print(n)
