import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft2, irfft2

#-----------------------------------------------------------#

# Function definitions and Global Variables
N = 1024    # Image Dimension
sigma = 25  # Sigma Value for Gaussian

# Gaussian Function (Point-Spread)
def gaussian(x, y, sigma):
    return np.exp(-(x**2 + y**2) / (2*sigma**2))

#-----------------------------------------------------------#

# Step 1: Read in the blurred photo

blurry_img = np.zeros((N, N))
with open("Projects/Image Deconvolution/blur.txt") as blur:
    for line_num, line in enumerate(blur):
        blurry_img[line_num] = np.array(line.split(" "))

#-----------------------------------------------------------#

# Step 2: Calculate the point spread function and create an array with it

# Create an empty array for the point spread function
point_spread = np.zeros((N, N))

# Populate the point spread array with the Gaussian function
for x in range(N):
    for y in range(N):
        # Use temporary variables for calculating the Gaussian value
        x_temp = x
        y_temp = y

        # Induce periodicity by wrapping around the midpoint of the array
        if x_temp > N // 2:
            x_temp -= N
        if y_temp > N // 2:
            y_temp -= N

        # Assign the Gaussian value to the point spread array
        point_spread[x, y] = gaussian(x_temp, y_temp, sigma)

#-----------------------------------------------------------#

# Step 3: Fourier Transform the blurred image and point-spread array

fft_blurred = rfft2(blurry_img)
fft_point_spread = rfft2(point_spread)

#-----------------------------------------------------------#

# Step 4: Compute the unblurred image transform as outlined on page 324 of the textbook

# Add a small constant to the denominator to avoid division by zero
fft_unblurred = fft_blurred / (N*N*(fft_point_spread + 1e-3))

#-----------------------------------------------------------#

# Step 5: Perform an inverse transform to get the unblurred photo

unblurred_img = irfft2(fft_unblurred)

#-----------------------------------------------------------#

# Step 6: Display the results

fig, (BLURRED, UNBLURRED, GAUSSIAN) = plt.subplots(figsize = (15, 15), nrows = 1, ncols = 3)

BLURRED.set_title('Blurred Image')
BLURRED.imshow(blurry_img, cmap='gray')

UNBLURRED.set_title('Unblurred Image')
UNBLURRED.imshow(unblurred_img, cmap='gray')

GAUSSIAN.set_title('Point-Spread Array')
GAUSSIAN.imshow(point_spread, cmap='gray')

plt.tight_layout()
plt.show()

"""
Question (from the textbook): 

What is it that limits our ability to deblur a photo? Why can we not perfectly unblur any photo and make it completely sharp?

Answer:

When an image is blurred, many of the higher fidelity details are lost. While we may employ fourier analysis techniques to 
deconvolve and recover many of the low to mid range details, the higher frequency details are unrecoverable. Also, because the
deconvolution process involves dividing by the Fourier Transform of the point-spread function, which may be very small for
certain frequencies, undesired features such as noise existing at these frequencies will be greatly amplified and lead to a 
sharper albeit noisy image. Another limitation in our ability to unblur an image has to do with our knowledge or lack thereof 
regarding the point-spread function resulting in the blur itself. In the example worked out above, we were given the PSF, but 
in many real-world scenarios the PSF may not be known and so trial and error is the way.

"""