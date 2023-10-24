import random as rd
import numpy as np

def EOverJ(a):
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
    return -1*s

#Generate a random lattice
n=10
lattice = np.zeros([n,n],int)
for i in range(n):
    for j in range(n):
        lattice[i][j]=1
        if rd.random()<0.5:
            lattice[i][j]=-1
print(lattice)

#Calculate energy change due to flipping element ij
i=5
j=0
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
print("Only consider terms that change:")
print("Eafter-Ebefore = ",deltaE)

#Calculate energy twice and take the difference
Ebefore=EOverJ(lattice)
lattice[i][j]*=-1
Eafter=EOverJ(lattice)
print("Calculate the energy twice and take the difference")
print("Eafter-Ebefore = ",Eafter-Ebefore)


    
    



