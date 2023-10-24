import matplotlib.pyplot as plt
import numpy as np
import math

x = np.loadtxt("height.txt",float)

mu=np.mean(x)
sigma=np.std(x)

plt.hist(x)
plt.xlabel("Height (in)")
plt.ylabel("Entries")
plt.title("Heights of Adult Males")
plt.text(60,100,"mean = %s" % round(mu,1))
plt.text(60,90,"Std Dev = %s"% round(sigma,1))
plt.savefig("Exercise2.png")
plt.show()
