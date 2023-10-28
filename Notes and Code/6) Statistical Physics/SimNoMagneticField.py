import random as rd
import numpy as np
import math

T = 1#in units of 1/kb
#T = 2
#T = 3
#T = 4

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

#Define starting lattice
n=10
lattice = np.zeros([n,n],int)
lattice += 1
print(lattice)
Ecurrent=Espin(lattice)
print("Starting energy = ",Ecurrent)

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

print(lattice)
print("Final energy: ",Ecurrent)
            

    


