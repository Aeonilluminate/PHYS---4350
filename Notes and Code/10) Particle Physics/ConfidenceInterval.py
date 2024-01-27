import random as rd
import math
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt

def f(x,c):
    return c

def chi2(y,c,sigma):
    s=0
    for i in range(len(y)):
        yexp=c
        term=((y[i] - c)**2)/(sigma[i]**2)
        s+=term
    return s

#generate data
yvals=np.zeros(100,float)
xvals=np.zeros(100,float)
sig=np.zeros(100,float)
for i in range(100):
    yvals[i] = rd.gauss(124,math.sqrt(124))
    sig[i] = math.sqrt(yvals[i])

#fit to a constant and get uncertainty with built-in function
pars,cov = op.curve_fit(f=f,xdata=xvals,ydata=yvals,p0=[0],sigma=sig,absolute_sigma=True)
print("Using scipy.optimize.curve_fit")
print("Fitted constant = ",pars[0])
print("Uncertainty = ", math.sqrt(cov[0][0]))
best = pars[0]
sigma = math.sqrt(cov[0][0])

cvals=np.linspace(100,150,1001)
chi2vals=[]
for val in cvals:
    chi2vals.append(chi2(yvals,val,sig))

plt.plot(cvals,chi2vals)
plt.xlabel("parameter")
plt.ylabel("$\chi^2$")
plt.show()

m=1e16
bestfit = 0
for i in range(len(cvals)):
    if chi2vals[i]<m:
        m=chi2vals[i]
        bestfit=cvals[i]
        minpoint=i


flag=0
i= minpoint
while flag==0:
    if (chi2vals[i]-m)>1:
        flag=1
        upval=cvals[i]
    i+=1
uperr = upval-bestfit

flag=0
i= minpoint
while flag==0:
    if (chi2vals[i]-m)>1:
        flag=1
        downval=cvals[i]
    i-=1
downerr = bestfit - downval

print("Using a grid search")
print("Fitted constant = ",bestfit)
print("Uncertainty = +",uperr,"-",downerr)

