import matplotlib.pyplot as plt
import numpy as np

#We plot a function by sampling points from the function
# The function we're going to plot is the height vs time of a projectile dropped from 100 m
# h=h_0 - 0.5gt^2

#over what range do you want to define the function?
xmin=0.
xmax=6.
#how many points?
npoints=600
#step size for sampling (i.e. distance between x-values)
dx=(xmax-xmin)/npoints
#define an array for the x-values
x=np.arange(xmin,xmax,dx)
#define the function
#x axis is time in s and y axis is height in m
#creates an array of y values according to this formula
y=100.-0.5*9.8*x**2

#ALWAYS label axes and provide the units 
plt.xlabel('time (s)')
plt.ylabel('height (m)')
#title of the plot
plt.title('Predicted Height vs Time')

#we want to draw a line, so we use plot
plt.plot(x,y, '-',lw=2)
#show gride lines
plt.grid(True)
#set axis limits
plt.ylim(0,110)
plt.xlim(-0.5,6)

#draw the plot
plt.show()
