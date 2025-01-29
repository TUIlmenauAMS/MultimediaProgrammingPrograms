#Program to plot the frequency magnitude of a 3-level Wavelet filter bank, using pulses into the synthesis filter bank.
#Gerald Schuller, January 2025

import pywt
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

def synthesis_wavelet_filter_bank(wavelet_name='db4', levels=3):
    """
    Synthesize a signal from wavelet coefficients using a wavelet filter bank.
    
    Args:
        wavelet_name (str): The name of the wavelet (e.g., 'db4').
        levels (int): Number of decomposition levels.

    Returns:
        None: Displays reconstruction process and result.
    """
    # Create a sample signal
    original_signal = np.sin(2 * np.pi * 5 * np.linspace(0, 1, 128)) + \
                      0.5 * np.sin(2 * np.pi * 15 * np.linspace(0, 1, 128))

    # Decompose signal into wavelet coefficients
    wavelet = pywt.Wavelet(wavelet_name)
    coeffs = pywt.wavedec(original_signal, wavelet, level=levels)
    print(f"Decomposed coefficients: {[len(c) for c in coeffs]}")
    #print("coeffs=", coeffs)
    
    for i in range(levels+1):
       for c in range(len(coeffs)):
          #print("c=", c)
          #print("coeffs[c].shape=", coeffs[c].shape)
          coeffs[c]=np.zeros(coeffs[c].shape)
          
       coeffs[i][10]=1.0
       # Reconstruction using waverec
       reconstructed_signal = pywt.waverec(coeffs, wavelet)

       # Ensure the reconstructed signal matches the original length
       reconstructed_signal = reconstructed_signal[:len(original_signal)]
       
       w,H=sp.freqz(reconstructed_signal)
       plt.plot(w, 20*np.log10(np.abs(H)+1e-4))
       #coeffs[c][10]=0.0 #for next iteration
    plt.title("Magnitude Frequency Response of " +str(levels)+ " level Daubechies Wavelet Filter Bank")
    plt.xlabel("Normalized frequency (pi is Nyquist frequency)")
    plt.ylabel("dB")
    #plt.savefig('wavelet_daubechies_3level_fr_syn.pdf')
    plt.show()
    
    """
    # Visualization
    plt.figure(figsize=(12, 8))

    # Original signal
    plt.subplot(3, 1, 1)
    plt.plot(original_signal, label='Original Signal')
    plt.title('Original Signal')
    plt.legend()
    plt.grid()

    # Reconstructed signal
    plt.subplot(3, 1, 2)
    plt.plot(reconstructed_signal, label='Reconstructed Signal', color='orange')
    plt.title('Reconstructed Signal from Wavelet Coefficients')
    plt.legend()
    plt.grid()

    # Difference
    plt.subplot(3, 1, 3)
    plt.plot(original_signal - reconstructed_signal, label='Difference', color='red')
    plt.title('Difference (Original - Reconstructed)')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()
    """
    

# Example usage
synthesis_wavelet_filter_bank(wavelet_name='db4', levels=3)

