import numpy as np


# copy()
arr= np.array([1,2,3,4,5])
x= arr.copy()
arr[0]=42

print(arr) # [42,2,3,4,5]
print(x)   # [1,2,3,4,5]


# view()

arr2 = np.array([1, 2, 3, 4, 5])
y= arr2.view()
arr2[0]= 56

print(arr2)
print(y)