import matplotlib.pyplot as plt
import numpy as np
import math
import sys

#Set up functions

#we're calling in chi^2, but it's actually not a chi^2.  We're using -2log-likelihood for Poisson statistics.
def chi2(y,yexp):
    s=0
    for i in range(len(y)):
        term = 2*(yexp[i] - y[i]*math.log(yexp[i]) + math.log(math.factorial(int(y[i]))))
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
data = np.loadtxt("NOvANueSample.txt",float)
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

th13vals=np.linspace(0,0.2,51)
m=1e6
bf=0
chi2vals=[]
for th13 in th13vals:
    pred = reweight(predsignal,energy,th13)
    pred += bkgd
    c2=chi2(observed,pred)
    chi2vals.append(c2)
    if c2<m:
        m=c2
        bf=th13
print("best fit value = ",bf)
plt.figure(2)
plt.plot(th13vals,chi2vals)
l=r'$\theta_{13}$ (radians)'
plt.xlabel(l)
l=r'$-2\ln L$'
plt.ylabel(l)

#plot predicted signal and background (for a particular value of theta13)
bestpred=reweight(predsignal,energy,bf)

plt.figure(3)
plt.hist([energy,energy],weights=[bkgd,bestpred],bins=bins,stacked=True,label=['Background','Best Fit Signal'])
plt.errorbar(energy,observed,yerr,xerr,lw=0,elinewidth=2,marker="o",label="Observed Events")
plt.ylim(0,30)
plt.xlim(0,5)
plt.ylabel("Number of events")
plt.xlabel("Neutrino Energy (GeV")
plt.title("Electron Neutrino Events in NOvA")
plt.legend()
plt.show()
