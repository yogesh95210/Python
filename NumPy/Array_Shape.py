import numpy as np

arr= np.array([[1,2,3,4,5],[9,8,7,6,5]])

print(arr.shape)   # (2,5)

arr2= np.array([1,2,3,4,5], ndmin=5)
print(arr2)
print("shape of array",arr2.shape)

# 1-D to 2-D 
arr3= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr= arr3.reshape(3,4)  #(dono ka multiply len og array hona cahiye)
newArr2= arr3.reshape(4,3)
newArr3= arr3.reshape(6,2)

print(newArr)
print(newArr2)
print(newArr3)

# 1-D to 3-D

Arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newArray = Arr.reshape(2, 3, 2)

print(newArray)