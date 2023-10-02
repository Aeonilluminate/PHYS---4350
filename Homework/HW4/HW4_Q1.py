import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define initial conditions and constants
x0, y0, z0 = 0, 0, 0
v0_x, v0_y, v0_z = 0, 550*math.sin(np.radians(37.)), 550*math.cos(np.radians(37.))
t0     = 0
g      = 9.81
DoverM = 2.3e-5

# choose step size
h=0.1

thetadeg=35.
theta=np.radians(thetadeg)

# function for variable air density
def fD(y):
    a = 6.5e-3
    b = 2.5
    T0 = 300
    return DoverM * (1 - a*y/T0)**b

# wind speed
vwind = 11.
vwind_x, vwind_y, vwind_z = vwind*math.sin(np.radians(22)), 0, vwind*math.cos(np.radians(22))
windlabel=r'11 m/s wind $22^\degree$ North of East'

xold = x0
yold = y0
zold = z0

vxold = v0_x
vyold = v0_y
vzold = v0_z

vproj_air_x = vxold - vwind_x
vproj_air_y = vyold - vwind_y
vproj_air_z = vzold - vwind_z
vproj_air = math.sqrt((vproj_air_x)**2 + (vproj_air_y)**2 + (vproj_air_z)**2)


xpoints = []
ypoints = []
zpoints = []
while yold>-0.1:
    xpoints.append(xold)
    ypoints.append(yold)
    zpoints.append(zold)

    xnew = xold + h*vxold
    ynew = yold + h*vyold
    znew = zold + h*vzold

    vxnew = vxold -h*fD(yold)*vproj_air*vproj_air_x
    vynew = vyold -h*g - h*fD(yold)*vproj_air*vproj_air_y
    vznew = vzold -h*fD(yold)*vproj_air*vproj_air_z

    xold = xnew
    yold = ynew
    zold = znew

    vxold = vxnew
    vyold = vynew
    vzold = vznew

    vproj_air_x = vxold - vwind_x
    vproj_air_y = vyold - vwind_y
    vproj_air_z = vzold - vwind_z
    vproj_air = math.sqrt((vproj_air_x)**2 + (vproj_air_y)**2 + (vproj_air_z)**2)

print("range with vwind = ",vwind,":",round(math.sqrt(xold**2 + zold**2)))
s=windlabel

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(zpoints, xpoints, ypoints)

ax.set_xlabel('z(t), East/West position (m)')
ax.set_ylabel('x(t), North/South position(m)')
ax.set_zlabel('y(t), Up/Down position(m)')
ax.set_title('Cannon Ball Trajectory with Wind')
ax.legend()

plt.show()

cannon_range = math.sqrt(xpoints[-1]**2 + zpoints[-1]**2)
cannon_dispN = xpoints[-1]

print(f"""
The range of the cannonball is {cannon_range} meters
The cannonball lands at a position that is {cannon_dispN} meters normal to the Eastward direction (positive z-axis)""")