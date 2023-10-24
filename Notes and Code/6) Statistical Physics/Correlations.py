import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt
import sys

Temps = [1.5,2,2.25,3,5]

nsweeps=1000

n=10
if n%2!=0:
    print("n must be even.")
    sys.exit()
halfn=int(n/2)

def Espin(a):
    Jconst=1
    #get number of rows and columns from input array
    row,col=a.shape
    s=0
    for i in range(row):#loop over rows
        for j in range(col):#sum over neighboring pairs in row i
            c=j+1#calculate index of the column to the right of current column
            #if we've reached the last column
            #use the first column as the column to the right of the last entry
            if c==col:
                c=0
            s+=a[i][j]*a[i][c]
    for j in range(col):#loop over columns
        for i in range(row):#sum over neighboring pairs in column j
            r=i+1#calculate index of row below the current row
            #if we've reached the last row
            #use the first row as the row below the last entry
            if r==row:
                r=0
            s+=a[i][j]*a[r][j]
    return -Jconst*s

def prob(d):
    return math.exp(-d/T)

def magnetization(a):
    row,col=a.shape
    return np.sum(a)/(row*col)


for T in Temps:
    print("T=",T)
    #Define starting lattice
    lattice = np.zeros([n,n],int)
    lattice += 1
    Ecurrent=Espin(lattice)
    #Initialize correlation function sum
    f = np.zeros([halfn+1],int)
    nterms = np.zeros([halfn+1],int)
    for k in range(nsweeps):
        #Loop over each spin in lattice
        for i in range(n):
            for j in range(n):
                rup=i-1#look at row above
                if rup==-1:
                    rup=n-1
                rdown=i+1# look at row below
                if rdown==n:
                    rdown=0
                cleft=j-1#look at column to the left
                if cleft==-1:
                    cleft=n-1
                cright=j+1#look at column to the right
                if cright==n:
                    cright=0
                deltaE = 2*lattice[i][j]*(lattice[rup][j] + lattice[rdown][j] + lattice[i][cleft] + lattice[i][cright])
                if deltaE<0:#flip it
                    lattice[i][j] *= -1
                    Ecurrent += deltaE
                else:#maybe we flip it?
                    if rd.random()<prob(deltaE):
                        lattice[i][j] *= -1
                        Ecurrent += deltaE

        #Loop over each spin in lattice again
        for i in range(n):
            for j in range(n):
                #print("lattice point: ",i,j)
                #first neighbors in same row
                r=i+1#start with one spin to the right
                if r==n:
                    r=0
                while r!=i:#keep going until we have cylced back to the starting spin
                    d=abs(r-i)#distance in the forward direction
                    d2=abs(d-n)#distance in the backward direction
                    dist=min(d,d2)#pick the minimum
                    f[dist] += lattice[i][j]*lattice[r][j]#calculate correlation and add to sum for average
                    nterms[dist] += 1
                    #print("neighbor: ",r,j,"distance = ",dist,"f = ",f[dist])
                    r += 1#look at the next row
                    if r==n:#if we reach the end of the row, start back at the beginnin
                        r=0
                #now neighbors in same column
                c=j+1
                if c==n:
                    c=0
                while c!=j:
                    d=abs(c-j)
                    d2=abs(d-n)
                    dist=min(d,d2)
                    f[dist] += lattice[i][j]*lattice[i][c]#calculate correlation and add to sum for average
                    nterms[dist] += 1
                    #print("neighbor: ",i,c,"distance = ",dist,"f = ",f[dist])
                    c += 1
                    if c==n:
                        c=0
    #calculate average
    favg=[]
    latticedist=[]
    for i in range(len(f)):
        if i!=0:
            favg.append(f[i]/nterms[i])
            latticedist.append(i)
    l="T="+str(T)
    plt.plot(latticedist,favg,marker="o",label=l)

   
plt.xlabel("i (Distance)")
l=r'f(i) = $\langle s_is_0\rangle$'
plt.ylabel(l)
plt.ylim(-0.1,1.1)
plt.legend()
l="Correlation function with a "+str(n)+"x"+str(n)+" Lattice"
plt.title(l)
plt.savefig("Correlations.png")
plt.show()
