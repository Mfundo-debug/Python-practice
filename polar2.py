"""
Find the equation of the polar curve r = 1 + cos(theta)
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def polar_curve(theta):
    return 1 + np.cos(theta)

if __name__ == '__main__':
    theta = np.linspace(0, 2 * np.pi, 1000)
    r = polar_curve(theta)
    plt.polar(theta, r)
    plt.show()
    
    # Find the equation of the polar curve
    theta = sp.symbols('theta')
    r = 1 + sp.cos(theta)
    print(f"The equation of the polar curve is r = {r}")