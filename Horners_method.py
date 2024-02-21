import numpy as np

x = int(input("Enter the value of x: "))

# the given polynomial
poly = 2 + x + 3 * np.power(x, 2) + 5 * np.power(x, 4)

#Using horner's method to evaluate the polynomial
res = 2 + x * (1 + x * (3 + x * (0 + x * (5))))

#Output
print("The result is ", res)