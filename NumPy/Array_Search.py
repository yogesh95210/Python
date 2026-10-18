import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)  # return a tuple (array([3, 5, 6],) --> means 4 is present at index 3,5 and 6


# find the indexes of odd values
arr = np.array([10, 14, 93, 41, 8, 7])
x = np.where(arr%2 == 1)
print(x)

# find the indexes of even values
arr = np.array([10, 14, 93, 41, 8, 7])
x = np.where(arr%2 == 0)
print(x)


# Search sorted method

# Find the indexes where the value 7 should be inserted:

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

# Search From the Right Side

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

# Multiple Values
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)