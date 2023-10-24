from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x=[]
y=[]
z=[]
for i in range(100):
    x.append(math.cos(i*math.pi/4))
    y.append(math.sin(i*math.pi/4))
    z.append(i)

ax.scatter(x,y,z,marker="^")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()
