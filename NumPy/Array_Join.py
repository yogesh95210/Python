import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)


# Stacking along Row
# hstack() method  (Horizontal stacking)

Arr1 = np.array([1, 2, 3])
Arr2 = np.array([4, 5, 6])

res= np.hstack((Arr1,Arr2))  # new way of concatination
print(res)

# vstack() method (vertical stacking)

array1= np.array([1,2,3])
array2= np.array([4,5,6])

final= np.vstack((array1,array2))

print(final)


#  Stacking along height
# dstack() method

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)