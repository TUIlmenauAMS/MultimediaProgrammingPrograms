#Program to plot the impulse response and magnitude frequency plot of the Daubechies Wavelet pair.
#Gerald Schuller, January 2025

#pip3 install PyWavelets
import pywt
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import freqz

# Define Daubechies (9,7) wavelet filters
wavelet = pywt.Wavelet('bior4.4')  # bior4.4 closely resembles Daubechies (9,7) structure

# Get filter coefficients
low_pass_analysis = wavelet.dec_lo
high_pass_analysis = wavelet.dec_hi

# Plotting the impulse responses
fig, ax = plt.subplots(figsize=(10, 6))

# Plot low-pass filter
x_low = np.arange(len(low_pass_analysis))
ax.plot(x_low, low_pass_analysis, label='Low-Pass Filter (Decimation)', linestyle='-', marker='o')

# Plot high-pass filter
x_high = np.arange(len(high_pass_analysis))
ax.plot(x_high, high_pass_analysis, label='High-Pass Filter (Decimation)', linestyle='--', marker='x')

# Formatting the plot
ax.set_title("Impulse Response of Daubechies (9,7) Filters", fontsize=14)
ax.set_xlabel("Index", fontsize=12)
ax.set_ylabel("Amplitude", fontsize=12)
ax.legend()
ax.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

# Compute the frequency response using freqz
w_low, h_low = freqz(low_pass_analysis)
w_high, h_high = freqz(high_pass_analysis)

# Convert to normalized frequencies (Nyquist = π)
freqs = w_low / np.pi  # Normalized frequency [0, 1]

# Plot the magnitude of the frequency responses
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(freqs, 20*np.log10(np.abs(h_low)), label='Low-Pass Filter Magnitude', linestyle='-', linewidth=2)
ax.plot(freqs, 20*np.log10(np.abs(h_high)), label='High-Pass Filter Magnitude', linestyle='--', linewidth=2)
ax.set_ylim([-90, 10])
# Formatting the plot
ax.set_title("Magnitude of Frequency Responses of Daubechies (9,7) Filters", fontsize=14)
ax.set_xlabel("Normalized Frequency (× π rad/sample), 1 is Nyquist frequency", fontsize=12)
ax.set_ylabel("Magnitude (dB)", fontsize=12)
ax.legend()
ax.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
