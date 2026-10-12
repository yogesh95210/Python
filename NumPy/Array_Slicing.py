
# Syntex  [start:end]  or [start:end:step]

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])


print(arr[1:5])  # [2,3,4,5]
print(arr[4:])   # [5,6,7]
print(arr[:4])   # [1,2,3,4]
print(arr[-3:-1]) # [5,6]
print(arr2[6:12:3]) # [7,10]

print(arr[::2])  # return every 2nd element from array ---> [1,3,5,7]