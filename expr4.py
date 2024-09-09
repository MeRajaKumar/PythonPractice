import numpy as np
# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr)
# arr[0,0],arr[1,0]=arr[1,0],arr[0,0]
# # arr[0,3],arr[1,0]=arr[1,3],arr[0,3]
# print(arr)

arr1 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr1)
arr1[0,0],arr1[0,3],arr1[1,0],arr1[1,3]=arr1[0,3],arr1[0,0],arr1[1,3],arr1[1,0]
print(arr1)
