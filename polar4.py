"""
given sphere coordinates, find the rectangular coordinates
constraints:
0 ≤ θ ≤ 2π
0 ≤ φ ≤ π
"""
import numpy as np
import matplotlib.pyplot as plt

def sphere_to_rect(r, theta, phi):
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    return x, y, z

if __name__ == '__main__':
    theta = np.linspace(0, 2*np.pi, 1000)
    phi = np.linspace(0, np.pi, 1000)
    theta, phi = np.meshgrid(theta, phi)
    r = 1
    x, y, z = sphere_to_rect(r, theta, phi)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, alpha=0.5)
    plt.title(r'$r = 1$')
    plt.show()