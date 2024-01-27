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

def PoissonLogL(t,ni,tau):
    s=0
    for i in range(len(t)):
        npred=ntot*dx*math.exp(-1*t[i]/tau)/tau
        term = ni[i]*math.log(npred) - math.log(math.factorial(int(ni[i]))) - npred
        s+= -2*term
    return s

#make a histogram
plt.figure(1)
(nobs,bs,patches) = plt.hist(vals,bins=bins)
plt.xlabel("Decay time (hrs)")
plt.ylabel("Number of counts")

#grid search tau at minimum chi2
gridn=81
tauvals=np.linspace(truetau-1,truetau+2,gridn)
cvals=np.zeros(gridn,float)
mincval=10000
for i in range(gridn):
    cvals[i] = PoissonLogL(tcenters,nobs,tauvals[i])
    if cvals[i]<mincval:
        mincval=cvals[i]
        besttau=tauvals[i]

#plot chi2
plt.figure(2)
plt.plot(tauvals,cvals)
plt.xlabel("Lifetime (hrs)")
plt.ylabel("Poisson log-likelihood")

print("True Lifetime = ",truetau)
print("Fitted Lifetime = ",besttau)
print("Function value at minimum = ",mincval)

ytrue = ntot*dx*np.exp(-tcenters/truetau)/truetau
yfit = ntot*dx*np.exp(-tcenters/besttau)/besttau

plt.figure(1)
plt.plot(tcenters,yfit,label="fitted curve")
plt.plot(tcenters,ytrue,label="true curve")
plt.legend()

plt.show()








##plt.figure(1)
##(n, bs, patches)=plt.hist(tvals,bins=bins)
##plt.xlabel("Decay time (hrs)")
##plt.ylabel("Number of counts")
##
##x=[]
##for i in range(len(n)):
##    x.append((bins[i]+bins[i+1])/2)#bin center
##
##bvals=np.linspace(0.8,2,100)
##cvals=[]
##for p in bvals:
##    a = nbins*binsize*(1/p)
##    cvals.append(PoissonLogL(x,n,a,p))
##
##plt.figure(2)
##plt.plot(bvals,cvals)
##plt.ylabel("-2lnL")
##plt.xlabel("Lifetime (hrs)")
##
##m=1e16
##l = 0
##for i in range(len(bvals)):
##    if cvals[i]<m:
##        m=cvals[i]
##        l=bvals[i]
##taufit = l
##print("Fitted Lifetime = ",taufit)
##
##xplot = np.linspace(x[0],x[len(x)-1],100)
##ytrue = truecurve(xplot,binsize,nhits,truetau)
##yfit = binsize*nhits*(1/taufit)*np.exp(-xplot/taufit)
##
##plt.figure(3)
##plt.hist(tvals,bins=bins,label="data")
##plt.plot(xplot,yfit,label="fitted curve")
##plt.plot(xplot,ytrue,label="true curve")
##plt.xlabel("Decay time (hrs)")
##plt.ylabel("Number of counts")
##plt.legend()
##
##plt.show()
