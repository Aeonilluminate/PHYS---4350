import numpy as np

def EOverJ(a):
    #get number of rows and columns from input array
    row,col=a.shape
    
    s=0
    for i in range(row):#loop over rows
        for j in range(col-1):#sum over neighboring pairs in row i
            s+=a[i][j]*a[i][j+1]
    for j in range(col):#loop over columns
        for i in range(row-1):#sum over neighboring pairs in column j
            s+=a[i][j]*a[i+1][j]

    return -1*s

print("Let's consider a 3x3 lattice, with all spins up (microstate 1)")
n=3
lattice = np.zeros([n,n],int)
lattice += 1
print(lattice)
E1=EOverJ(lattice)
print("E1 = ",E1)

print("Now let's consider a microstate where all spins are up except for the center spin (microstate 2)")
lattice[1][1]=-1
print(lattice)
E2=EOverJ(lattice)
print("E2 = ",E2)

print("E1-E2 = ",E1-E2)

lattice[1][1]=1#return this to original value

print("Now let's consider a microstate where all spins are up except for one edge spin (microstate 3)")
lattice[0][1]=-1
print(lattice)
E3=EOverJ(lattice)
print("E3 = ",E3)

print("E1-E3 = ",E1-E3)
