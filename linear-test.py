"""
Write a script that models data points and fit the linear regression and plots it.
- Make sure to add the uncertainty in the graph +_2 standard deviation
- Make sure to add the R^2 value in the graph
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate some data
np.random.seed(0)
x = np.random.rand(100, 1)
y = 2 + 3 * x + np.random.rand(100, 1)

# Fit the model
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

# Plot the data
plt.figure(figsize=(10, 5))
plt.scatter(x, y, s=10)
plt.plot(x, y_pred, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()

# Print the R^2 value
print('R^2:', r2_score(y, y_pred))

# plot the uncertainty
plt.figure(figsize=(10, 5))
plt.scatter(x, y, s=10)
plt.plot(x, y_pred, color='r')
plt.fill_between(x.ravel(), y_pred.ravel() - 2, y_pred.ravel() + 2, color='red', alpha=0.2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression with uncertainty')
plt.show()
