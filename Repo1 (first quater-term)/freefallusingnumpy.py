import numpy


 # Take the user's input for initial values 
h = float(input("Enter the initial height in meters: "))
g = float(input("Enter the value for gravity in meters per second (the one used for Earth is 9.81ms^-1): ")or 9.81)

t = numpy.linspace(0, 5, num=6)


# Formula to calculate the point at which the ball is found at time = t
y = h - 0.5*g*t**2  # Where y is Vertica position, h is height, t is time, g is acceleration due to gravity

# Difference in position from each y
numpy.diff(y)

# Average of differences
numpy.mean(y)

# Print the results for height at t, the difference in those points, and the average of those differences
print (y)
print(numpy.diff(y))
print(numpy.mean(y))