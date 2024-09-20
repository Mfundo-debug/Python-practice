import numpy as np

# define the function to be integrated

def integrand(x, y):
    return (x - y) / (np.pi * x - y * np.pi**2)

#number of random samples
N = 100000

# generate random samples for x and y
x_samples = np.random.uniform(0, 1, N)
y_samples = np.random.uniform(0, 1, N)

# evaluate the integrand at the random samples
integrand_values = integrand(x_samples, y_samples)

# compute the average of the integrand values
integral_approx = np.mean(integrand_values)

# since we are integrating over a unit square , the area is 1
# so the integral approximation is just the average value

print(integral_approx)