import numpy as np
import math
import matplotlib.pyplot as plt
import cmath
import numpy.fft as fft

y = np.loadtxt("Notes and Code\9) Fourier Analysis\dow.txt",float)

plt.figure(1)
plt.plot(y)
plt.ylabel("Daily Closing Value for the Dow Jones Industrial Average")
plt.xlabel("Days")
plt.title("Dow average, 2006-2010")

plt.show()

c = fft.rfft(y)
cmag=abs(c)

plt.figure(2)
plt.plot(cmag)
plt.ylabel("$|c_k|$")
plt.xlabel("k")
plt.title("FFT Coefficients")

plt.show()

n = len(c)
print(n," coeffcients")
ntokeep=100
#ntokeep=50
#ntokeep=10
#ntokeep=2
print("Keeping ",ntokeep)

for i in range(ntokeep,n):
    c[i]=0

ynew = fft.irfft(c)

plt.figure(3)
plt.plot(y,label="No Smoothing")
plt.plot(ynew,label="With Smoothing")
plt.ylabel("Daily Closing Value for the Dow Jones Industrial Average")
plt.xlabel("Days")
plt.title("Dow average, 2006-2010")

plt.legend()
plt.show()


