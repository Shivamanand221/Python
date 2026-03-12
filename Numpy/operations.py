import numpy as np

arr1= np.random.rand(4,4)
print(arr1)

arr2= np.arange(1,9)    
print("reshaped array is ", arr2.reshape(2,4))

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

np.mean(a, axis=1)

print(np.max(a))
print(np.argmax(a))

arr3= np.array([10,20,30,40,50])
print(arr3[arr3>25])

x = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(x[x>5])
print(x[:, 0:2])