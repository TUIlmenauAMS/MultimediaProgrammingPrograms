#Program to compute and plot the cubic B-Spline basis function and compute and display a z-plane plot.
#Gerald Schuller, January 2025

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# Define knots, control points, and degree for a cubic B-Spline
#knots = [ 0, 1, 2, 3, 4,5,6,7,8,9,10]
knots = [ 0,0,0,0, 1, 2, 3, 4,4,4,4] #defining the interval boundaries 
control_points = np.array([0, 0,0,1,0,0,0])
degree = 3

# Create B-Spline object
bspline = BSpline(knots, control_points, degree, extrapolate=False) #only points with 4 overlapping basis functions

# Generate x values and corresponding y values
x = np.linspace(0, 10, 500)
y = bspline(x)

# Define interval boundaries
intervals = [0, 1, 2, 3, 4, 5, 6, 7]

# Plot the cubic B-Spline
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Cubic B-Spline Curve", color='blue')
plt.scatter(intervals, bspline(intervals), color="red", label="Interval Points")
for i in range(len(intervals) - 1):
    plt.axvline(intervals[i], color="gray", linestyle="--", linewidth=0.8)
plt.axvline(intervals[-1], color="gray", linestyle="--", linewidth=0.8, label="Intervals")
plt.title("Cubic B-Spline Curve with Marked Intervals")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.legend()
#plt.grid()
plt.savefig("b_spline.png")
plt.show()

from zplaneplot import zplaneplot
denominator = [1]  # FIR filter has no poles except at the origin
numerator=y[:200] #B-spline
#print("numerator=", numerator)

zplaneplot(numerator, denominator)

