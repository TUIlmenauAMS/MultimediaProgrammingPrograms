#pip3 install PyWavelets
import pywt
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread('DSC04998.JPG')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

# Perform 3-level wavelet decomposition
coeffs = pywt.wavedec2(image, 'haar', level=3)

# Extract the subband shapes for plotting
subband_shapes = [coeffs[0].shape] + [c[0].shape for c in coeffs[1:]]
canvas_height = sum([s[0] for s in subband_shapes])
canvas_width = sum([s[1] for s in subband_shapes])
canvas = np.zeros((canvas_height, canvas_width))

# Place the subband images in the correct relative positions
current_x, current_y = 0, 0

canvas[:coeffs[0].shape[0], :coeffs[0].shape[1]] = coeffs[0]/np.max(coeffs[0])
current_y += coeffs[0].shape[0]
current_x += coeffs[0].shape[1]

for i in range(1, len(coeffs)):
    cH, cV, cD = coeffs[i]
    h, w = cH.shape
    canvas[current_y:current_y+h, : w] = np.abs(cH)/np.max(np.abs(cH)) #below
    canvas[:h, current_x:current_x+w] = np.abs(cV) /np.max(np.abs(cV))#to the right
    canvas[current_y:current_y+h, current_x:current_x+w] = np.abs(cD)/np.max(np.abs(cD)) #diagonal
    current_x += w
    current_y += h
# Plot the result
plt.figure(figsize=(10, 10))
plt.imshow(canvas, cmap='gray')
plt.title('Wavelet Subband Decomposition')
plt.axis('off')
plt.show()

