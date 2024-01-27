import matplotlib.pyplot as plt
import numpy as np

datam = np.loadtxt("eventdisplaydata1.txt",float)
timem = datam[:,0]
wirem = datam[:,1]
energym = datam[:,2]

plt.figure(1)
plt.scatter(timem,wirem)
plt.ylabel("vertical")
plt.xlabel("drift")
plt.title("Simulated Atmospheric Muon Neutrino in DUNE")

datae = np.loadtxt("eventdisplaydata2.txt",float)
timee = datae[:,0]
wiree = datae[:,1]
energye = datae[:,2]

plt.figure(2)
plt.scatter(timee,wiree)
plt.ylabel("vertical")
plt.xlabel("drift")
plt.title("Simulated Atmospheric Electron Neutrino in DUNE")
plt.show()
