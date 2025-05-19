import numpy as np
import sympy as sp

# Define symbols
x = sp.Symbol('x')

# Example equation
equation = x**2 - 3*x + 2

# Solve the equation
solutions = sp.solve(equation, x)

print(solutions)
