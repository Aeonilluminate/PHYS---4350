import random as rd
import math


acube=8#area of the cube
n=10**5
k=0
for i in range(n):
    x=rd.uniform(-1,1)
    y=rd.uniform(-1,1)
    z=rd.uniform(-1,1)
    if x**2 + y**2 + z**2 <= 1:#inside the sphere
        k+=1
p=k/n
asphere=p*acube

print("True value: ",4*math.pi/3)
print("Answer with Monte Carlo method: ",asphere)

