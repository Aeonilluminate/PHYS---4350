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

#calculate chi2 (comparing probability densities)
def chi2(t,ni,tau):
    s=0
    for i in range(len(t)):
        npred=ntot*dx*math.exp(-1*t[i]/tau)/tau
        if ni[i]>0:
            term = (ni[i]-npred)**2/ni[i]
        else:
            term=0
        s+=term
    return s


#make a histogram
plt.figure(1)
(nobs,bs,patches) = plt.hist(vals,bins=bins)
plt.xlabel("Decay time (hrs)")
plt.ylabel("Number of counts")

#grid search tau at minimum chi2
gridn=81
tauvals=np.linspace(truetau-2,truetau+2,gridn)
cvals=np.zeros(gridn,float)
mincval=10000
for i in range(gridn):
    cvals[i] = chi2(tcenters,nobs,tauvals[i])
    if cvals[i]<mincval:
        mincval=cvals[i]
        besttau=tauvals[i]

#plot chi2
plt.figure(2)
plt.plot(tauvals,cvals)
plt.xlabel("Lifetime (hrs)")
plt.ylabel("chi-squared")

print("True Lifetime = ",truetau)
print("Fitted Lifetime = ",besttau)
print("Chi-squared at minimum = ",mincval)

ytrue = ntot*dx*np.exp(-tcenters/truetau)/truetau
yfit = ntot*dx*np.exp(-tcenters/besttau)/besttau

plt.figure(1)
plt.plot(tcenters,yfit,label="fitted curve")
plt.plot(tcenters,ytrue,label="true curve")
plt.legend()

plt.show()
