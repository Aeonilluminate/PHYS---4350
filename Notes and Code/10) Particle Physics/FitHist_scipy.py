import numpy as np
import math
import matplotlib.pyplot as plt
import cmath
import sys
import scipy.optimize as op

#load data, measured decay times
vals = np.loadtxt("histdata.txt",float)
ntot = len(vals)

#values
truetau=2.3#used to generate data
dx=2.0#bin size
nbins=15
minx=0
maxx=30
#bin edges
bins=np.linspace(minx,maxx,nbins+1)
#center of each bin
tcenters = (bins[:-1] + bins[1:]) / 2

#function we are fitting to
def expo(x,N0,tau):
    return N0*np.exp(-x/tau)

#make a histogram
(nobs, bs, patches)=plt.hist(vals,bins=bins,label="data")
plt.xlabel("Decay time (hrs)")
plt.ylabel("Number of counts")

#make arrays needed for fitting function
#only include bins with non-zero counts
x=[]
y=[]
sig=[]
for i in range(len(nobs)):
    if nobs[i]>0:
        y.append(nobs[i])
        sig.append(math.sqrt(nobs[i]))
        x.append((bins[i]+bins[i+1])/2)#bin center

#do the fit
pars,cov = op.curve_fit(f=expo,xdata=x,ydata=y,p0=[0,1],bounds=((-np.inf,0.1),(np.inf,np.inf)),sigma=sig,absolute_sigma=True)

#results
print("True Lifetime = ",truetau)
print("Fitted Lifetime = ",pars[1])
print("True N0 = ",ntot*dx/truetau)
print("Fitted N0 = ", pars[0])

#plot curves
ytrue = ntot*dx*np.exp(-tcenters/truetau)/truetau 
yfit = pars[0]*np.exp(-tcenters/pars[1])

plt.plot(tcenters,yfit,label="fitted curve")
plt.plot(tcenters,ytrue,label="true curve")
plt.xlabel("Decay time (hrs)")
plt.ylabel("Number of counts")
plt.legend()

plt.show()
