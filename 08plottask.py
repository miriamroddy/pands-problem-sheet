## Write a program called plottask.py that displays:
## a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
## and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes. Some marks will be given for making the plot look nice (legend etc).

## We import the numpy library and give it the alias np (for ease of reference) and do the same with the matplotlib library, giving it the alias plt.

import numpy as np
import matplotlib.pyplot as plt


## We generate 1000 random values from a normal distro with mean 5 and SD of 2. The generated values are stored in the data variable - we want an array that contains 1000
## random numbers with a mean of 5 and an SD of 2.

data = np.random.normal(5, 2, 1000)

## Now that we have the 1000 values we want, we want to create a histogram of what we have stored in the data variable.  Data refers to the array we just created. Bins=30 specifies
##  the number of bins or columns that we want in the histogram. The last argument specifies the transparency of the bars in the histrogram. 
## 0.5 means we will have semi-transparent bars i.e. 50% transparency. The label argument defines what we use in the final legend.

plt.hist(data, bins=30, alpha=0.5, label='Normal Distribution')

## We need to create a second array, called x, that contains a hundred evenly spaced values between 0 and 10 using the numpy.linspace() method. The third argument specifies the number of values to generate in the sequence.

x = np.linspace(0, 10, 100)

# We calculate the function h(x) = x^3 for each value of x

y = x ** 3

# Plot the function h(x) on the same graph with a red label - the plt is an alias for the mathplotlib library

plt.plot(x, y, color='red', label='h(x) = x^3')

# Add labels to both axes

plt.xlabel('X')
plt.ylabel('Frequency / h(x)')

## We want to give the graph a title and to include a legend

plt.title('Task 8: Histogram of Normal Distribution and Plot of h(x) = x^3')
plt.legend()

# Finally, we show the resulting graph

plt.show()
