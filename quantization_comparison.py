#Program to demonstrate quantization artifacts for DCT coefficients.
#Gerald Schuller, January 2025

#pip3 install scikit-image
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.util import view_as_blocks
from scipy.fftpack import dct, idct
from imageio import imread

# Load example image and convert to grayscale
#image = img_as_float(data.camera())

pic = imread('DSC04998.JPG')
# Convert to luminance (Y channel)
image = 0.299 * pic[:, :, 0] + 0.587 * pic[:, :, 1] + 0.114 * pic[:, :, 2]
image=image[1000:1128,1000:1128]/np.max(np.abs(image))
#print(np.max(image))
#print(image.shape)
# Define block size for DCT
block_size = 8

# Function to apply DCT and quantization
def apply_dct_and_quantization(image, quantization_matrix):
    # Divide image into non-overlapping blocks
    blocks = view_as_blocks(image, block_shape=(block_size, block_size))
    compressed_blocks = np.zeros_like(blocks)

    # Perform DCT, quantization, and reconstruction block by block
    for i in range(blocks.shape[0]):
        for j in range(blocks.shape[1]):
            block = blocks[i, j]
            dct_block = dct(dct(block.T, norm='ortho').T, norm='ortho')
            quantized_block = np.round(dct_block / quantization_matrix)
            dequantized_block = quantized_block * quantization_matrix
            compressed_blocks[i, j] = idct(idct(dequantized_block.T, norm='ortho').T, norm='ortho')

    # Combine blocks back into a single image
    compressed_image = np.block(
        [[compressed_blocks[i, j] for j in range(compressed_blocks.shape[1])]
         for i in range(compressed_blocks.shape[0])]
    )
    return compressed_image

# Define quantization matrices Q
fine_quantization = np.full((block_size, block_size), 0.2)
coarse_quantization = np.full((block_size, block_size), 0.8)

# Apply DCT and quantization
fine_quantized_image = apply_dct_and_quantization(image, fine_quantization)
coarse_quantized_image = apply_dct_and_quantization(image, coarse_quantization)

# Plot original, fine, and coarse quantized images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(fine_quantized_image, cmap='gray')
plt.title("Fine Quantization")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(coarse_quantized_image, cmap='gray')
plt.title("Coarse Quantization")
plt.axis("off")

# Save the plot as an image (optional)
# plt.savefig("quantization_comparison.png")

# Show the plot
plt.show()

