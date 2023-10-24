import numpy as np
import math
import matplotlib.pyplot as plt

#constants
V=1#Volts

#number of grid points, 0-100 in increments of 1 is 101 points
n=101

#make the grid
phi = np.zeros([n,n],float)
phinew = np.zeros([n,n],float)
#set the top edge (first row) to a fixed value of V
for i in range(n):
    phi[0][i] = V
#print(phi)

#target accurancy
e=1e-3
#initialize diff
diff=100

nsteps=0#count how many iterations until convergence
while diff>e:
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:# values on the boundary are fixed
                phinew[i][j] = phi[i][j]
            else:
                phinew[i][j] = (phi[i+1][j] + phi[i-1][j] + phi[i][j+1]+phi[i][j-1])/4
    diff=np.max(abs(phinew-phi))
    print(diff)
    phi=np.copy(phinew)
    nsteps+=1

#print(phi)
print(nsteps,"steps")

#plot with a weighted 2D histogram
x=[]
y=[]
w=[]
for i in range(n):
    for j in range(n):
        x.append(j)#j=0 (left column) is equivalent to x=0
        y.append(100-i)#i=0 (top row) is equivalent to y=100
        w.append(phi[i][j])

b=np.arange(-0.5,101.5,1)#bin edges from -0.5 to 100.5, so there's one bin for every point on the grid
plt.hist2d(x,y,weights=w,bins=b)
plt.xlabel("x (cm)")
plt.ylabel("y (cm)")
plt.axis("square")
plt.xlim(-0.5,100.5)
plt.ylim(-0.5,100.5)
c = plt.colorbar()
c.set_label("Potential (V)")
plt.show()

