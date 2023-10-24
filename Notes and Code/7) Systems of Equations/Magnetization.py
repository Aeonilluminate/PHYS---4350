import numpy as np
import math
import matplotlib.pyplot as plt

def f(M,T,z):
    return math.tanh(z*M/T)
def fprime(M,T,z):
    return z/(T*(math.cosh(z*M/T)**2))

z=4
Mag=[]
Temps = np.linspace(0.1,z+1,100)
target=1e-6
for T in Temps:
    #initial guess
    M = 1
    epsilonp=100
    while abs(epsilonp)>target:
        Mp=f(M,T,z)
        epsilonp=(M-Mp)/(1-1/fprime(M,T,z))
        M=Mp
    Mag.append(Mp)

plt.plot(Temps,Mag,lw=2)
label=r'Temperature (1/$k_B$)'
plt.xlabel(label)
plt.ylabel("Magnetization")
plt.show()
