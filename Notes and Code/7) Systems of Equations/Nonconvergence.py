import numpy as np
import math

#initial guess
xguess=0.5

for i in range(100):
    x=math.exp(1-xguess**2)
    diff=xguess-x
    xguess=x
    print(x)
