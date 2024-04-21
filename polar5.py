"""
given radius = 5, find the area of the circle and the circumference
find the equation of the circle in rectangular form
"""
import numpy as np
import matplotlib.pyplot as plt

def polar_to_rect(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

if __name__ == '__main__':
    theta = np.linspace(0, 2*np.pi, 1000)
    r = 5
    x, y = polar_to_rect(r, theta)
    plt.plot(x, y)
    plt.title(r'$r = 5$')
    plt.show()
    area = np.pi * r**2
    circumference = 2 * np.pi * r
    print(f'Area: {area}')
    print(f'Circumference: {circumference}')
    print(f'Equation in rectangular form: x^2 + y^2 = 25')