import matplotlib.pyplot as plt

#Suppose we have these measurements for the height vs time of a projectile dropped from 100 m
t = [0.0,1.0,2.0,3.0,4.0]#time in seconds
h = [100., 92.3, 83.6, 56.8, 19.0]#measured height in meters

#ALWAYS label axes and provide the units 
plt.xlabel('time (s)')
plt.ylabel('height (m)')
#title of the plot
plt.title('Measured Height vs Time')

#we want to show the data points (no line connecting them), so we use scatter
plt.scatter(t,h,color="black",marker="o",s=30)
#show gride lines
plt.grid(True)
#set axis limits
plt.ylim(0,110)
plt.xlim(-0.5,6)

#draw the plot
plt.show()
