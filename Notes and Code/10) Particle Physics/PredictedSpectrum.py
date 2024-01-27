import matplotlib.pyplot as plt
import numpy as np
import math
import sys

#Set up functions

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

#bin info
binwidth=0.5
bins=np.linspace(1,4,7)

#plot predicted signal and background (for a particular value of theta13)
plt.figure(1)
plt.hist([energy,energy],weights=[bkgd,predsignal],bins=bins,stacked=True,label=["Background","Signal"])
plt.ylim(0,100)
plt.xlim(0,5)
plt.ylabel("Number of events")
plt.xlabel("Neutrino Energy (GeV")
plt.title("Selected Electron Neutrino Sample")
l=r'$\theta_{13} = 0.3$'
plt.text(0.5,90,l)
plt.legend()

th13=0.2
pred=reweight(predsignal,energy,th13)

#plot predicted signal and background (for a particular value of theta13)
plt.figure(2)
plt.hist([energy,energy],weights=[bkgd,pred],bins=bins,stacked=True,label=["Background","Signal"])
plt.ylim(0,100)
plt.xlim(0,5)
plt.ylabel("Number of events")
plt.xlabel("Neutrino Energy (GeV")
plt.title("Selected Electron Neutrino Sample")
l=r'$\theta_{13} = $'+str(th13)
plt.text(0.5,90,l)
plt.legend()

plt.show()

