import random as rd
import numpy as np
import sys

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

def magnetization(a):
    row,col=a.shape
    return np.sum(a)/(row*col)

ntrials=1000
n=20
half=int(n*n/2)
avge=0
for i in range(ntrials):
    lattice = np.zeros([n,n],int)
    lattice += 1
    #randomly choose half to be -1
    ndown=0
    while ndown<half:
        b1=rd.randrange(n)
        b2=rd.randrange(n)
        if lattice[b1][b2]>0:#if it's up
            lattice[b1][b2] *= -1# flip it
            ndown += 1
    E1=EOverJ(lattice)/(n**2)#divide by n^2 to get energy per spin
    avge+=E1/ntrials#get average energy per spin over all the trials
    if i==0:
        print(lattice)
        print("E/J = ",E1)
        M=magnetization(lattice)
        print("M = ",M)

print("Average Energy per spin = ",avge)


