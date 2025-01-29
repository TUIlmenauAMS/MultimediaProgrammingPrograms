import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk
import pywt

def zplaneplot(numerator, denominator):
   #Computes the zeros and poles of a transfer function defined by the numerator and denominator coefficients.
   #and plots them in the complex z-transform plane
   #Arguments: numerator, denominator
   
   # Compute poles, zeros, and gain
   zeros, poles, _ = tf2zpk(numerator, denominator)
   print("abs(zeros)=", abs(zeros))

   # Create a unit circle for reference
   theta = np.linspace(0, 2 * np.pi, 1000)
   unit_circle = np.exp(1j * theta)

   # Plot the z-plane
   plt.figure(figsize=(6, 6))
   plt.plot(unit_circle.real, unit_circle.imag, 'k--', label='Unit Circle')  # Unit circle
   plt.scatter(zeros.real, zeros.imag, s=50, color='blue', label='Zeros')  # Zeros
   plt.scatter(poles.real, poles.imag, s=50, color='red', marker='x', label='Poles')  # Poles

   # Add grid and labels
   plt.axhline(0, color='k', linewidth=0.5)
   plt.axvline(0, color='k', linewidth=0.5)
   plt.title('Pole-Zero Plot') # of Daubechies Highpass Filter
   plt.xlabel('Re')
   plt.ylabel('Im')
   plt.grid()
   plt.legend(loc='upper right')
   plt.axis('equal')
   plt.show()
   return

if __name__ == '__main__':
   # Define Daubechies highpass filter coefficients (example: Daubechies 'db4')
   # Replace these coefficients with actual values for the highpass filter

   wavelet_name = 'db4'
   wav = pywt.Wavelet(wavelet_name)
   print(wav)
   dec_lo, dec_hi = wav.dec_lo, wav.dec_hi
   #print("deec_hi=", dec_hi)
   #print("deec_lo=", dec_lo)
   #plt.plot(dec_hi, label="dec_hi")
   #plt.plot(dec_lo, label="dec_lo")
   #plt.legend()
   #plt.show()

   numerator = dec_hi  # Highpass filter
   denominator = [1]  # FIR filter has no poles except at the origin

   zplaneplot(numerator, denominator)

   #plt.savefig('zplane_daubechies.png', dpi=300)

