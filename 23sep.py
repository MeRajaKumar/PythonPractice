import matplotlib.pyplot as plt
import numpy as np
x = np.array([2,4,6,8,10,12,14,16])
y = np.array([2,4,16,8,10,34,19,16])
plt.bar(x,y)
x1=np.array([23,34,45,6,6,2,33,45])
y1=np.array([23,34,45,6,6,2,33,45])
plt.bar(x1,y1)
plt.xlabel("hindi")
plt.ylabel("english")
plt.show()