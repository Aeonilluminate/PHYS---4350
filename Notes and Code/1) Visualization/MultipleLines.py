import matplotlib.pyplot as plt
import numpy as np

# Let's draw both the measured points and the predicted curve for the height vs time of a projectile dropped from 100 m (on the same plot)

#define the function as before
xmin=0.
xmax=6.
npoints=600
dx=(xmax-xmin)/600
x=np.arange(xmin,xmax,dx)
y=100.-0.5*9.8*x**2

#here are the measured points as before
t = [0.0,1.0,2.0,3.0,4.0]#time in seconds
h = [100., 92.3, 83.6, 56.8, 19.0]#measured height in meters

#ALWAYS label axes and provide the units 
plt.xlabel('time (s)')
plt.ylabel('height (m)')
#title of the plot
plt.title('Height vs Time')

#draw both
#Use 'label' to set what will show up in the legend
plt.plot(x,y, '-',lw=2,color="red",label="Predicted")
plt.scatter(t,h,label="Measured",color="black",marker="o",s=30)
plt.grid(True)
plt.ylim(0,110)
plt.xlim(-0.5,6)
plt.legend()#draw the legend
plt.savefig("overlapping.png")#save it as a png (this command must come before the show command)
plt.show()
