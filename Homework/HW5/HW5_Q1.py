import numpy as np
import math
import matplotlib.pyplot as plt
import random as rd

rd.seed(44)

PI = math.pi
nsteps = 100
nwalkers = 500

plt.figure(1, figsize=(10, 10))


Rav = np.zeros(nsteps)
Rav2 = np.zeros(nsteps)
xvals = [0]
yvals = [0]

for j in range(nwalkers):

    x, y, R = 0, 0, 0

    for n in range(nsteps):
        theta = 2 * PI * rd.random()
        x += math.cos(theta)
        y += math.sin(theta)
        R = math.sqrt(x**2 + y**2) 
        Rav[n] += R/nwalkers
        Rav2[n] += R**2/nwalkers
        if j == 1:
            xvals.append(x)
            yvals.append(y)

# Compute the differences between consecutive x and y values
dx = np.diff(xvals)
dy = np.diff(yvals)

# Create a colormap and normalize based on the number of steps
cmap = plt.get_cmap('jet')
norm = plt.Normalize(0, nsteps)

# Use normalized sequence to map each step to a color
colors = [cmap(norm(value)) for value in range(nsteps)]


# Plot the quiver plot with gradient colors
plt.quiver(xvals[:-1], yvals[:-1], dx, dy, color=colors, angles='xy', scale_units='xy', scale=1)

# Plot the points with gradient colors
plt.scatter(xvals, yvals, color=colors + [cmap(norm(nsteps))], s=30, edgecolor='black', linewidth=0.5)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Random Walk with Gradient")

plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Add colorbar to show the gradient
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, label='Step Number')



plt.figure(2, figsize=(10, 10))
plt.title(r'$\langle r^2 \rangle$ vs $n$ Average Squared Distance vs Step Number (over 500)')
plt.xlabel('n (Step Number)')
plt.ylabel(r'$\langle r^2 \rangle$')
plt.plot(Rav2)

plt.show()