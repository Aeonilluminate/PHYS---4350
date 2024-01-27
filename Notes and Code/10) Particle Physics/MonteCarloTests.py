import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.optimize as op
import scipy.stats as st
import numpy.random as nprd

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
normfit = pars[0]
taufit = pars[1]

#calculate expected content in each bin based on best fit distribution
xcalc = np.array(x,float)
yfit = pars[0]*np.exp(-xcalc/pars[1])

#do the chi2 test
chisq,p = st.chisquare(y,yfit,2)
chi2fit = chisq
print("Chi-squared from our best fit = ",chi2fit)
dof = len(y) - len(pars)
print("Degrees of freedom = ",dof)
cpd = chi2fit/dof
print("Chi-squared per degree of freedom = ",cpd)
print("p-value = ",p)

ntrials=1000
c=[]
ngreater=0
norm=normfit
tau=taufit
plt.figure(2)
for trial in range(ntrials):
    #simulate a new data set by drawing randomly from an exponential
    #distribution with a lifetime of our best fit value
    tpts=[]
    for hit in range(ntot):
        tpts.append(nprd.exponential(taufit))
    #make a histogram
    (n, bs, patches)=plt.hist(tpts,bins=bins)
    #select bins to use in fit
    x=[]
    y=[]
    sig=[]
    for i in range(len(n)):
        if n[i]>=5:
            y.append(n[i])
            sig.append(math.sqrt(n[i]))
            x.append((bins[i]+bins[i+1])/2)#bin center
    #do the fit
    pars,cov = op.curve_fit(f=expo,xdata=x,ydata=y,p0=[norm,tau],bounds=((-np.inf,0.1),(np.inf,np.inf)),sigma=sig,absolute_sigma=True)
    #results
    norm = pars[0]
    tau = pars[1]
    #calculate expected content in each bin based on best fit distribution
    xcalc = np.array(x,float)
    yfit = norm*np.exp(-xcalc/tau)
    #calculate chi2 for this data set
    chisq,p = st.chisquare(y,yfit,2)
    c.append(chisq)
    #count the number of times the chi-square is worse than for our data set
    if chisq>chi2fit:
        ngreater+=1

plt.figure(3)
bins2 = np.linspace(0,15,61)
plt.hist(c, bins=bins2)
plt.xlabel("$\chi^2$ from each pseudo-experiment")
plt.ylabel("Number of entries")

print("p-value from simulated chi-squared distribution: ",ngreater/ntrials)

plt.show()

