#Program to plot some 8x8 2D DCT basis images.
#Gerald Schuller, January 2025
 
import numpy as np
import matplotlib.pyplot as plt

# Function to generate basis images for the 2D DCT
def generate_dct_basis(size, u, v):
    """Generates the (u, v) basis function for a 2D DCT of given size."""
    x = np.arange(size)
    y = np.arange(size)
    X, Y = np.meshgrid(x, y)
    basis = (
        np.cos(np.pi * u * (2 * X + 1) / (2 * size))
        * np.cos(np.pi * v * (2 * Y + 1) / (2 * size))
    )
    # Normalization factor
    if u == 0:
        basis *= np.sqrt(1 / size)
    else:
        basis *= np.sqrt(2 / size)

    if v == 0:
        basis *= np.sqrt(1 / size)
    else:
        basis *= np.sqrt(2 / size)

    return basis

# Parameters
size = 8  # Block size
indices_with_dc = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (3,3)]  # Include DC subband

# Generate and plot the basis functions including the DC subband
plt.figure(figsize=(12, 8))
for i, (u, v) in enumerate(indices_with_dc, start=1):
    basis = generate_dct_basis(size, u, v)
    plt.subplot(2, 3, i)
    plt.imshow(basis, cmap='gray', extent=[0, size, 0, size])
    plt.title(f"Basis Function (u={u}, v={v})")
    plt.colorbar()
    plt.axis("off")

plt.suptitle("2D DCT Subbands Including DC (u=0, v=0)", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure (optional)
#plt.savefig("dct_subbands_with_dc.png")

# Show the plot
plt.show()

