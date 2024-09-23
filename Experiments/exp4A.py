import numpy as np
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
print("Before swaping the colounms:")
print(arr1)
arr1[0,0],arr1[0,3],arr1[1,0],arr1[1,3]=arr1[0,3],arr1[0,0],arr1[1,3],arr1[1,0]
print("After swaping the colounms:")
print(arr1)
