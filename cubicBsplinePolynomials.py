#pip3 install sympy
from sympy import symbols, Piecewise, integrate, simplify, And, pprint, piecewise_exclusive, latex

# Define variables
x, u = symbols('x u') #x: global variable, u: local variable

# Define the box function h_1(x)
h_1 = Piecewise((1, And(x >= 0, x < 1)), (0, True))

# Convolution function with explicit bounds
def convolve(f1, f2):
    return integrate(f1.subs(x, u) * f2.subs(x, x - u), (u, -float('inf'), float('inf')))

# Compute h_2(x) = h_1(x) * h_1(x)
h_2 = convolve(h_1, h_1)
# Compute h_3(x) = h_2(x) * h_1(x)
h_3 = convolve(h_2, h_1)
# Compute h_4(x) = h_3(x) * h_1(x)
h_4 = convolve(h_3, h_1)

# Manually define the intervals for the cubic B-spline over the unit interval 0<=u<=1:
Q_1 = simplify(h_4.subs(x, 0 + u).rewrite(Piecewise)) #shift to unit interval
Q_2 = simplify(h_4.subs(x, 1 + u).rewrite(Piecewise))
Q_3 = simplify(h_4.subs(x, 2 + u).rewrite(Piecewise))
Q_4 = simplify(h_4.subs(x, 3 + u).rewrite(Piecewise))

# Print the cubic B-spline polynomials for each interval
# keep only a unit interval using box function
print("Cubic B-Spline (h_4) Polynomials for Each Interval:")
print("Look for the interval 0=<t<1")
print("First interval:")
Q_1=simplify((Q_1*(h_1.subs(x,u))).rewrite(Piecewise)) 
Q_1= piecewise_exclusive(Q_1)
pprint(Q_1)
print(latex(Q_1))

print("2nd interval:")
Q_2=simplify((Q_2*(h_1.subs(x,u))).rewrite(Piecewise))
Q_2= piecewise_exclusive(Q_2)
pprint( Q_2)
print(latex(Q_2))

print("3rd interval:")
Q_3=simplify((Q_3*(h_1.subs(x,u))).rewrite(Piecewise))
Q_3= piecewise_exclusive(Q_3)
pprint( Q_3)
print(latex(Q_3))

print("4th interval:")
Q_4=simplify((Q_4*(h_1.subs(x,u))).rewrite(Piecewise))
Q_4= piecewise_exclusive(Q_4)
pprint( Q_4)
print(latex(Q_4))
