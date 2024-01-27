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
data = np.loadtxt("NOvANueSample.txt",float)
#this gives the center of each energy bin
energy = data[:,0]
#observed dtata
observed = data[:,1]
#predicted background
bkgd = data[:,2]
bkgd *= 6
#predicted signal for a value of theta13=0.3
predsignal = data[:,3]

nexp=1000
th13vals=np.linspace(0,0.2,51)
fractions=[]
for j in range(len(th13vals)):
    print("'True' value of theta_13: ",th13vals[j])
    
    #expected number of events at 'true' value of th13
    predtrue = reweight(predsignal,energy,th13vals[j])
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
    
plt.plot(th13vals,fractions)
plt.hlines(0.683,0,0.2,color="black",label="0.683")
plt.hlines(0.90,0,0.2,color="red",label="0.90")
plt.hlines(0.955,0,0.2,color="orange",label="0.955")
l=r'$\theta_{13}$ (radians)'
plt.xlabel(l)
plt.ylabel("Fraction of pseudo-experiments with a better fit")
plt.legend()
plt.show()

#find confidence interval
#conflevel=0.683
conflevel=0.9
flag=0
for i in range(len(fractions)):
    if flag==1:
        break
    if fractions[i]<conflevel:
        print("Lower bound: ",th13vals[i])
        low=th13vals[i]
        for j in range(i+1,len(fractions)):
            if fractions[j]>conflevel:
                print("Upper bound: ",th13vals[j])
                high=th13vals[j]
                flag=1
                break

print("theta_13 = ",round(bfdata,3), "+",round(high-bfdata,3),"-",round(bfdata-low,3),"at the ",round(conflevel*100,3)," confidence level")
