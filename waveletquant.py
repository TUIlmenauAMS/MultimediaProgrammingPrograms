#Program to demonstrate quantization artifacts for Wavelet coefficients, using the Ilmenau test image.
#Gerald Schuller, January 2025

#pip3 install scikit-image
#pip3 install PyWavelets

import pywt
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.color import rgb2gray
from skimage.util import img_as_float
from imageio.v2 import imread

def quantize(coeffs, step_size):
    """Quantizes the wavelet coefficients."""
    return [np.round(c / step_size) * step_size for c in coeffs]

def reconstruct_image(coeffs, wavelet):
    """Reconstructs the image from wavelet coefficients."""
    return pywt.waverec2(coeffs, wavelet)

# Load test image and convert to grayscale
#image = img_as_float(rgb2gray(data.camera()))
image = rgb2gray(imread('DSC04998.JPG')/ 255.0)
image=image[1000:1128,1000:1128] #keep zoom in

# Perform a 3-stage wavelet decomposition
wavelet = 'bior4.4'
coeffs = pywt.wavedec2(image, wavelet, level=3)
#print("coeffs=", coeffs)

# Apply fine and coarse quantization
fine_quant_coeffs = [quantize(c, step_size=0.2) for c in coeffs]
coarse_quant_coeffs = [quantize(c, step_size=0.8) for c in coeffs]

# Reconstruct images
fine_reconstructed = reconstruct_image(fine_quant_coeffs, wavelet)
#fine_reconstructed = reconstruct_image(coeffs, wavelet)
coarse_reconstructed = reconstruct_image(coarse_quant_coeffs, wavelet)

# Plot original and reconstructed images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis('off')

axes[1].imshow(fine_reconstructed, cmap='gray')
axes[1].set_title("Reconstructed (Fine Quantization)")
axes[1].axis('off')

axes[2].imshow(coarse_reconstructed, cmap='gray')
axes[2].set_title("Reconstructed (Coarse Quantization)")
axes[2].axis('off')

plt.tight_layout()
plt.show()

