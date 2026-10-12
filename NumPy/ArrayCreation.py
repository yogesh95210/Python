import numpy as np

arr= np.array([1,2,3,4,5])
print(arr)
print(type(arr))  # <class 'numpy.ndarray'>

# Tuple to array

arr2= np.array((1,2,3,4,5,6))
print(arr2)

# 0-D Array

zero_d_array= np.array(56)
print(zero_d_array)
print(type(zero_d_array))

# 1-D Array

one_d_array= np.array([8,3,1,4,10])
print(one_d_array)

# 2-D Array

two_d_array= np.array([[1,2,3],[6,5,4]])
print(two_d_array)

# 3-D Array

three_d_array= np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(three_d_array)