import numpy as np
import math
import matplotlib.pyplot as plt
import numpy.fft as fft

y = np.loadtxt("note.txt",float)

Dt = 1/44.1e3
N = len(y)#want a power of 2 since we will use FFT
L = N*Dt

#calculate coefficients
c = fft.rfft(y)
#magnitude
cmag=abs(c)

k_dominant = list(cmag).index(max(cmag))
print(f"Dominant k value is {k_dominant}")
print(f"Frequency of Note played is {k_dominant/L}")
print(f"The name of the note being played is C5")

T = np.arange(0, L, Dt)
plt.figure(1)
plt.plot(T, y)
plt.ylabel("Wave Amplitude")
plt.xlabel("Time")
plt.title("Waveform of note.txt")

plt.figure(2)
plt.plot(cmag,lw=0,marker="o")
plt.ylabel("$c_k$")
plt.xlabel("k")
plt.title("DFT Coefficients")


plt.show()