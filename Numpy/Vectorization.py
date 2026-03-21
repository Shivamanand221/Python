import numpy as np

v1=np.array([[1, 2, 3, 4, 5]])
print(v1*3+1)
print(v1**2+1)

a = np.array([1,2,3])
b = np.array([10,20,30])
print(a+b)

#Normalize
n1= (v1-np.min(v1))/(np.max(v1)-np.min(v1))
print(n1)