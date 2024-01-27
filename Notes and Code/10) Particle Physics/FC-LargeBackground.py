import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import numpy.random as npg

#Set up functions

#we're calling in chi^2, but it's actually not a chi^2.  We're using -2log-likelihood for Poisson statistics.
def chi2(y,yexp):
    s=0
    for i in range(len(y)):
        term = 2*(yexp[i] - y[i]*math.log(yexp[i]))
        s+=term
    return s

#approximation for numu->nue oscillation probability, i.e. nue appearance from numus
def probapp(e,theta13):
    theta23=0.86
    dm2 = 2.41e-3
    L = 810
    p = (math.sin(theta23)**2)*(math.sin(2*theta13)**2)*(np.sin(1.27*dm2*L/e)**2)
    return p

#we know the prediction at some particular value of theta13, so we can scale by the ratio of probabilities to get the prediction at a different value of theta13
def reweight(p,e,theta13):
    ratio = np.zeros(len(e),float)
    ratio = probapp(e,theta13)/probapp(e,0.3)
    return ratio*p

#input file
data = np.loadtxt("LargeBackground.txt",float)
#this gives the center of each energy bin
energy = data[:,0]
#observed dtata
observed = data[:,1]
#predicted background
bkgd = data[:,2]
#predicted signal for a value of theta13=0.3
predsignal = data[:,3]

#for error bars on plot
#horizontal error bar is just the bin width
#vertical error bar is statistical uncertainty (square root of the number of events in the bin)
xerr=np.zeros(len(energy),float)
xerr += 0.25
yerr=np.sqrt(observed)

#bin info
binwidth=0.5
bins=np.linspace(1,4,7)

#plot data and predicted background
plt.figure(1)
plt.hist(energy,weights=bkgd,bins=bins,label="Predicted Background")
plt.errorbar(energy,observed,yerr,xerr,lw=0,elinewidth=2,marker="o",label="Observed Events")
plt.ylim(0,30)
plt.xlim(0,5)
plt.ylabel("Number of events")
plt.xlabel("Neutrino Energy (GeV")
plt.title("Electron Neutrino Events in NOvA")
plt.legend()
plt.show()

nexp=1000
th13vals=np.linspace(0,0.2,51)
#only interested in significance at theta13=0
th13truevals=[0]
fractions=[]
for j in range(len(th13truevals)):
    #expected number of events at 'true' value of th13
    predtrue = reweight(predsignal,energy,th13truevals[j])
    predtrue += bkgd
    
    #find delta-chi2 for data
    minchi2=1e6
    bfval=0
    for i in range(len(th13vals)):
        pred = reweight(predsignal,energy,th13vals[i])
        pred += bkgd
        c2=chi2(observed,pred)
        if c2<minchi2:
            minchi2=c2
            bfval=th13vals[i]
    chi2attrue = chi2(observed,predtrue)
    deltachi2_obs=chi2attrue-minchi2
    bfdata = bfval
    print(bfdata)

    #repeat for pseudo-experiments and count how many have better chi2 than data
    count=0
    for k in range(nexp):
        #generate pseudo-experiments by randomly pulling from "true" distribution
        obs=[]
        for i in range(len(predtrue)):
            obs.append(npg.poisson(predtrue[i]))
        #find deltachi2 for this pseudo-experiment
        minchi2=1e6
        bfval=0
        for i in range(len(th13vals)):
            pred = reweight(predsignal,energy,th13vals[i])
            pred += bkgd
            c2=chi2(obs,pred)
            if c2<minchi2:
                minchi2=c2
                bfval=th13vals[i]
        chi2attrue = chi2(obs,predtrue)
        deltachi2_pseudo=chi2attrue-minchi2
        #does this pseudo-experiment have better chi2 than data?
        if deltachi2_pseudo<deltachi2_obs:
            count += 1
    fractions.append(count/nexp)
    
print("theta_13=0 is allowed at the ",round(fractions[0]*100,3)," confidence level")
print("(Means it's excluded at any higher confidence levels)")

