import numpy as np
import math

#initial guess
xguess=0.5

for i in range(100):
    x=math.sqrt(1-math.log(xguess))
    diff=xguess-x
    xguess=x
    print(x)
