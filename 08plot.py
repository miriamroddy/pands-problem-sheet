import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
data = np.random.normal(5, 2, 1000)

# Create a histogram of the data
plt.hist(data, bins=30, alpha=0.5, label='Normal Distribution')

# Create an array of x values in the range [0, 10] with 100 points
x = np.linspace(0, 10, 100)

# Calculate the function h(x) = x^3
y = x ** 3

# Plot the function h(x) on the same set of axes
plt.plot(x, y, color='red', label='h(x) = x^3')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Frequency / h(x)')
plt.title('Histogram of Normal Distribution and Plot of h(x) = x^3')
plt.legend()

# Show the plot
plt.show()
