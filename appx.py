import numpy as np
from scipy.optimize import fsolve

# Define the polynomial equation
def equation(y):
    return 2*y**4 - 4*y**3 + y**2 + 1

# Initial guesses for the roots
initial_guesses = [0, 1, -1, 2]

# Find the roots
roots = fsolve(equation, initial_guesses)

# Filter out complex roots and duplicates
real_roots = np.unique(np.round(roots[np.isreal(roots)], 5))

# Calculate corresponding x values
x_values = real_roots - real_roots**2

# Print the solutions
for y, x in zip(real_roots, x_values):
    print(f"y = {y}, x = {x}")
