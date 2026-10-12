import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr2= np.array([1,2,3,4],dtype='S')
print(arr2)
print(arr2.dtype)


# convert data type

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr2 = np.array([1.1, 2.1, 3.1])
newarr2= arr2.astype(int)
print(newarr2)
print(newarr2.dtype)

arr3 = np.array([1, 0, 3])
newarr3 = arr3.astype(bool)
print(newarr3)
print(newarr3.dtype)