import numpy as np
import math
import matplotlib.pyplot as plt
import cmath
import sys

data = np.loadtxt("lineardata2.txt",float)
y1=data[:,1]
x1=data[:,0]
sigma1=data[:,2]

ssqinv = 1/sigma1**2
xoverssq = x1*ssqinv
xsqoverssq = xoverssq*x1
yoverssq = y1*ssqinv
prod = x1*y1*ssqinv

denom = np.sum(ssqinv)*np.sum(xsqoverssq) - np.sum(xoverssq)*np.sum(xoverssq)

b = (np.sum(xsqoverssq)*np.sum(yoverssq) - np.sum(xoverssq)*np.sum(prod))/denom
a = (np.sum(ssqinv)*np.sum(prod) - np.sum(xoverssq)*np.sum(yoverssq))/denom

sigmab = math.sqrt(np.sum(xsqoverssq)/denom)
sigmaa = math.sqrt(np.sum(ssqinv)/denom)

print("slope = ",a," +- ",sigmaa)
print("y-intercept = ",b," +- ", sigmab)



