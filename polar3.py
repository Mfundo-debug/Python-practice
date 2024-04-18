"""
Given the polar equation sin(3θ) = 1/2, find the rectangular equation.
constraints:
0 ≤ θ ≤ 2π
"""

import numpy as np
import matplotlib.pyplot as plt

def polar_to_rect(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

if __name__ == '__main__':
    theta = np.linspace(0, 2*np.pi, 1000)
    r = 1/(2*np.sin(3*theta))
    x, y = polar_to_rect(r, theta)
    plt.plot(x, y)
    plt.title(r'$\sin(3\theta) = \frac{1}{2}$')
    plt.show()