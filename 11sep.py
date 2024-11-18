import numpy as np
# arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
arr=np.array([[[1,2,3,4,5]]]) #3 2d array
arr=np.array([])
for x in arr:
     for y in x:
          for j in y:
               print(j)