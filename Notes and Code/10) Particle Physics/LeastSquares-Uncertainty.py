import numpy as np
import math
import matplotlib.pyplot as plt
import cmath
import sys

data = np.loadtxt("lineardata2.txt",float)
y1=data[:,1]
x1=data[:,0]
sigma1=data[:,2]

plt.figure(1)
plt.plot(x1,sigma1,lw=0, marker="o")
plt.ylabel("Uncertainty in measurement of y")
plt.xlabel("x")

ssqinv = 1/sigma1**2
xoverssq = x1*ssqinv
xsqoverssq = xoverssq*x1
yoverssq = y1*ssqinv
prod = x1*y1*ssqinv

denom = np.sum(ssqinv)*np.sum(xsqoverssq) - np.sum(xoverssq)*np.sum(xoverssq)

b = (np.sum(xsqoverssq)*np.sum(yoverssq) - np.sum(xoverssq)*np.sum(prod))/denom
a = (np.sum(ssqinv)*np.sum(prod) - np.sum(xoverssq)*np.sum(yoverssq))/denom
print("Weighting by uncertainty")
print("slope = ",a)
print("y-intercept = ",b)
yfit = a*x1 + b

sigma1=np.zeros(len(x1),float)
sigma1+=1

ssqinv = 1/sigma1**2
xoverssq = x1*ssqinv
xsqoverssq = xoverssq*x1
yoverssq = y1*ssqinv
prod = x1*y1*ssqinv

denom = np.sum(ssqinv)*np.sum(xsqoverssq) - np.sum(xoverssq)*np.sum(xoverssq)

b = (np.sum(xsqoverssq)*np.sum(yoverssq) - np.sum(xoverssq)*np.sum(prod))/denom
a = (np.sum(ssqinv)*np.sum(prod) - np.sum(xoverssq)*np.sum(yoverssq))/denom
print("Setting sigma_i = 1")
print("slope = ",a)
print("y-intercept = ",b)
yfit2 = a*x1 + b

plt.figure(2)
plt.plot(x1,y1,lw=0,marker="o",label="data")
plt.plot(x1,yfit,lw=2,label="weighted by uncertainty")
plt.plot(x1,yfit2,lw=2,label="equal weights")
plt.ylabel("y")
plt.xlabel("x")
plt.ylim(0,46)
plt.legend()

plt.show()
