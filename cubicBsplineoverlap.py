#Program to demonstrate overlap of cubic B-Spline functions for interpolation.
#Gerald Schuller, January 2025

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# Define sample points at integer x-values
#x = np.arange(-2, 6)
x=np.arange(7)
#y = np.array([0, 1, 4, 3, 2, 5, 4, 3])  # Example values
y = np.arange(7)
#y = np.ones(7)

# Define a uniform knot vector with clamped endpoints
k = 3  # Cubic B-spline
#t = np.concatenate(([x[0]]*(k), x, [x[-1]]*(0) ))
#t=np.arange(-3,7) #knots
t=np.arange(-2,8)
print("t=", t)

# Create B-Spline basis functions
spl = BSpline(t, np.eye(len(x)), k, extrapolate=False)

t_eval = np.linspace(x[0]-1, x[-1]+1, 200)
plt.figure(figsize=(8, 6))

# Plot B-Spline basis functions
for i in range(len(x)):
    plt.plot(t_eval, spl(t_eval)[:, i], label=f'h_4(t-{i})')

plt.title("Overlap of Cubic B-Spline Basis Functions")
plt.xlabel("t")
plt.ylabel("Basis Function Value")
plt.legend()
#plt.grid()
plt.axvline(1, color="gray", linestyle="--", linewidth=0.8, label="Intervals")
plt.axvline(2, color="gray", linestyle="--", linewidth=0.8, label="Intervals")
plt.axvline(3, color="gray", linestyle="--", linewidth=0.8, label="Intervals")
plt.savefig("b_spline_overlap.pdf")
plt.show()

# Interpolation using cubic B-Spline
coefficients = y  # Use y directly as coefficients
interp_spline = BSpline(t, coefficients, k)

# Plot interpolated function along with control points
plt.figure(figsize=(8, 6))
plt.plot(t_eval, interp_spline(t_eval), label='Cubic B-Spline', color='blue')
plt.scatter(x, y, color='red', label='Control Points')
plt.title("Cubic B-Spline Interpolation")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

