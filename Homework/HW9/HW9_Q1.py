import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

def process_list(lst):

    singleton_lists = []

    for index, value in enumerate(lst):
        new_list = [0] * len(lst)
        new_list[index] = value
        singleton_lists.append(new_list)

    return singleton_lists

data = np.loadtxt("data.txt",float)
t, y = data[:, 0], data[:, 1]

plt.figure(1)
plt.plot(t, y)
plt.ylabel("Function + Noise (y)")
plt.xlabel("Seconds (t)")
plt.title("Function + Noise vs Time")

plt.show()

c = fft.rfft(y)
cmag=abs(c)

plt.figure(2)
plt.plot(cmag)
plt.ylabel("$|c_k|$")
plt.xlabel("k")
plt.title("FFT Coefficients")

plt.show()

n = len(c)
print(n," coeffcients")
ntokeep=10
print("Keeping ",ntokeep)

for i in range(ntokeep,n):
    c[i]=0


coeff_lists = process_list(c)

n = 1
epsilon = 1e-8
coefficient_data = {}

for coeff in coeff_lists:
    inverse_transform_data = fft.irfft(coeff)
    reference = inverse_transform_data[0]

    for index, value in enumerate(inverse_transform_data[1:]):
        if reference - epsilon < value < reference + epsilon:
            period = 2*index
            try: 
                frequency = 1/period
            except:
                frequency = 'No Frequency Detected'
            break
    
    if type(frequency) == float:
        coefficient_data[f"k={n-1}"] = {"INDEX": n-1, "DATA": inverse_transform_data,
                                        "AMPLITUDE": round(max(inverse_transform_data), 3), 
                                        "PERIOD": round(period, 5), "FREQUENCY": round(frequency, 5)}
    else:
        coefficient_data[f"k={n-1}"] = {"INDEX": n-1, "DATA": inverse_transform_data,
                                        "AMPLITUDE": round(max(inverse_transform_data), 3), 
                                        "PERIOD": round(period, 5), "FREQUENCY": frequency}    
    
    plt.figure(2 + n)
    plt.plot(coefficient_data[f"k={n-1}"]['DATA'])
    plt.ylim((-5, 5))
    plt.ylabel("y")
    plt.xlabel("t")
    plt.title(f"SIN WAVE k={n-1}, A={coefficient_data[f'k={n-1}']['AMPLITUDE']}, f={coefficient_data[f'k={n-1}']['FREQUENCY']}")
    plt.show()
    n += 1
    if n > ntokeep:
        break
    
ynew = fft.irfft(c)

plt.figure(2 + n)
plt.plot(y,label="No Smoothing")
plt.plot(ynew,label="With Smoothing")
plt.ylabel("Function (y)")
plt.xlabel("Seconds (t)")
plt.title("Function with Smoothing")

plt.figure(3 + n)
plt.plot(ynew, label = "Smoothed Function")
for plot_data in coefficient_data.values():
    plt.plot(plot_data["DATA"], label = f"SIN WAVE, k={plot_data['INDEX']}, A = {plot_data['AMPLITUDE']}, f = {plot_data['FREQUENCY']}")
    plt.ylim((-5, 5))
    plt.ylabel("Function Values (y)")
    plt.xlabel("Seconds (t)")
    plt.title("Function with Corresponding Wave Components")

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.subplots_adjust(right=0.75) # Adjust the subplot to make room for the legend

# Show the plot
plt.show()