#Program to demonstrate B-Spline interpolation and approximation.
#Gerald Schuller, January 2025

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline #for pre-distortion of control points
from scipy.interpolate import BSpline #original B-Spline

# Define sample points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1]) #function points

# Define a finer grid for interpolation
x_fine = np.linspace(x.min(), x.max(), 300)

# Create B-Spline representation, with pre-distortion of control points
spl = make_interp_spline(x, y, k=3)  # k=3 indicates cubic B-Spline
print("y=", y)
print("spl.c=", spl.c)
controlpoints=spl.c #adapted or pre-distorted control points
knots=spl.t #knots
print("knots=", knots)
degree=spl.k 
# Create B-Spline object
bspline = BSpline(knots, y, k=degree, extrapolate=False) #function points as control points

# Evaluate the B-Splines on the fine grid
y_fine = spl(x_fine) #with pre-distortion
y_fine_b_spline = bspline(x_fine) #without adaptated control points or pre-distortion

# Plot original points and interpolated curve
plt.figure(figsize=(8, 4))
plt.plot(x, y, 'o', label='Sample Points')
plt.plot(x_fine, y_fine, '-', label='B-Spline Interpolation with Adapted Control Points')
plt.plot(x_fine, y_fine_b_spline, '-', label='B-Spline appr. with Function Values as Control Points')
plt.legend()
plt.title('B-Spline Interpolation Example')
plt.xlabel('x intervals')
plt.ylabel('y')
plt.grid()
plt.savefig("B-spline_interpolation.png")
plt.show()
