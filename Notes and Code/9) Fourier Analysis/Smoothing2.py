import numpy as np
import math
import matplotlib.pyplot as plt
import cmath
import numpy.fft as fft
import sys

def f(t):
    if (int(2*t))%2==0:
        return 1
    else:
        return -1


tvals=np.linspace(0,1,1000)
fvals=list(map(f,tvals))

c = fft.rfft(fvals)
cmag=abs(c)

plt.figure(1)
plt.plot(cmag)
plt.ylabel("$|c_k|$")
plt.xlabel("k")
plt.title("FFT Coefficients")

plt.show()

n = len(c)
print(n," coeffcients")
ntokeep=n
#ntokeep=300
#ntokeep=100
#ntokeep=50
#ntokeep=10
#ntokeep=5
print("Keeping ",ntokeep)

for i in range(ntokeep,n):
    c[i]=0

ynew = fft.irfft(c)

plt.figure(2)
plt.plot(tvals,fvals,label="No Smoothing")
plt.plot(tvals,ynew,label="With Smoothing")
plt.ylabel("f(t)")
plt.xlabel("t")
plt.title("Square wave")

plt.legend()
plt.show()


