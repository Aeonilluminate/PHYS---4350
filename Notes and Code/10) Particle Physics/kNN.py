import numpy as np
import math
import matplotlib.pyplot as plt
import sys

#read in data
numuccdata = np.loadtxt("numutrain.txt",float)
nuedata = np.loadtxt("nuetrain.txt",float)

maxL_mu = numuccdata[:,0]
nshowers_mu = numuccdata[:,1]
ntracks_mu = numuccdata[:,2]
nclusters_mu = numuccdata[:,3]

maxL_nue = nuedata[:,0]
nshowers_nue = nuedata[:,1]
ntracks_nue = nuedata[:,2]
nclusters_nue = nuedata[:,3]

bound = len(maxL_mu)
print(bound)

#put them all the same array; first 1000 will be numu, second 1000 will be nue
maxL_all = np.concatenate([maxL_mu,maxL_nue])
nshowers_all = np.concatenate([nshowers_mu,nshowers_nue])
ntracks_all = np.concatenate([ntracks_mu,ntracks_nue])
nclusters_all = np.concatenate([nclusters_mu,nclusters_nue])

#normalize
Lnorm=max(maxL_all)
Tnorm=max(ntracks_all)
Snorm=max(nshowers_all)
Cnorm=max(nclusters_all)
ntracks_all = ntracks_all/Tnorm
nshowers_all = nshowers_all/Snorm
maxL_all = maxL_all/Lnorm
nclusters_all = nclusters_all/Cnorm

#plot variables
plt.figure(1)
plt.plot(nclusters_mu,maxL_mu,marker="o",color="blue",lw=0,label="numu")
plt.plot(nclusters_nue,maxL_nue,marker="o",color="red",markersize=2,lw=0,label="nue")
plt.xlabel("Number of clusters")
plt.ylabel("Length of longest track (cm)")
plt.legend()
plt.figure(2)
plt.plot(ntracks_mu,maxL_mu,marker="o",color="blue",lw=0,label="numu")
plt.plot(ntracks_nue,maxL_nue,marker="o",color="red",markersize=2,lw=0,label="nue")
plt.xlabel("Number of tracks")
plt.ylabel("Length of longest track (cm)")
plt.legend()
plt.figure(3)
plt.plot(nshowers_mu,maxL_mu,marker="o",color="blue",lw=0,label="numu")
plt.plot(nshowers_nue,maxL_nue,marker="o",color="red",markersize=2,lw=0,label="nue")
plt.xlabel("Number of showers")
plt.ylabel("Length of longest track (cm)")
plt.legend()
plt.show()

#set k
k=25

#read in test data
numuccdata2 = np.loadtxt("numutest.txt",float)
nuedata2 = np.loadtxt("nuetest.txt",float)

maxL_mu2 = numuccdata2[:,0]
nshowers_mu2 = numuccdata2[:,1]
ntracks_mu2 = numuccdata2[:,2]
nclusters_mu2 = numuccdata2[:,3]

maxL_nue2 = nuedata2[:,0]
nshowers_nue2 = nuedata2[:,1]
ntracks_nue2 = nuedata2[:,2]
nclusters_nue2 = nuedata2[:,3]

bound2 = len(maxL_mu2)
print(bound2)

#put them all the same array; first half will be numu, second half will be nue
maxL_all_test = np.concatenate([maxL_mu2,maxL_nue2])
nshowers_all_test = np.concatenate([nshowers_mu2,nshowers_nue2])
ntracks_all_test = np.concatenate([ntracks_mu2,ntracks_nue2])
nclusters_all_test = np.concatenate([nclusters_mu2,nclusters_nue2])

numuscores=[]
nuescores=[]
for w in range(len(maxL_all_test)):
    if w%100==0:
        print(w)
        
    maxL = maxL_all_test[w]/Lnorm
    ns = nshowers_all_test[w]/Snorm
    nt = ntracks_all_test[w]/Tnorm
    nc = nclusters_all_test[w]/Cnorm
    
    alld=[]
    alli=[]
    for i in range(len(maxL_all)):
        dist=math.sqrt((maxL-maxL_all[i])**2 + (nc-nclusters_all[i])**2 + (ns - nshowers_all[i])**2 + (nt - ntracks_all[i])**2)
        alld.append(dist)
        alli.append(i)

    #zip them together
    zipped = zip(alld,alli)
    #sort based on distances
    sorted_zipped = sorted(zipped)
    #unzip them
    sorted_dist = [i for i, j in sorted_zipped]
    sorted_i = [j for i, j in sorted_zipped]
    
    nnumu=0
    nnue=0
    for i in range(k):
        if sorted_i[i]<bound:
            nnumu+=1
        else:
            nnue+=1
    if w<bound2:#true numu
        numuscores.append(nnumu/k)
    else:
        nuescores.append(nnue/k)

bins = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
plt.figure(4)
(nmuhist, bs, patches)=plt.hist(numuscores,bins=bins)
plt.xlabel("numu scores")
plt.title("True numu events")
plt.figure(5)
(nehist, bs, patches)=plt.hist(nuescores,bins=bins)
plt.xlabel("nue scores")
plt.title("True nue events")

print(len(nmuhist),len(nehist))
countm=0
counte=0
for i in range(6,len(nmuhist)):
    countm += nmuhist[i]/np.sum(nmuhist)
    counte += nehist[i]/np.sum(nehist)
    
print("If we require a score of at least 0.5 for classification, then:")
print(countm," of muon neutrino events are identified correctly ")
print(counte," of electron neutrino events are identified correctly ")

plt.show()


