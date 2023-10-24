import numpy as np
import math

#initial guess
xguess=1
diff=1e5
while abs(diff)>1e-12:
    x=2 - math.exp(-1*xguess)
    diff=xguess-x
    xguess=x
    print(x)
