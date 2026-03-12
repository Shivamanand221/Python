import numpy as np

print(np.arange(1,11)) 
print(np.zeros([3,4], dtype=np.int8)) 
print(np.ones([5,2], dtype=np.int8)) 

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

a1 = np.array([[10,20,30],
              [40,50,60]])

print("Shape is ", a1.shape) 
print("No. of dimentions are ",a1.ndim) 
print("Row 1 = ", a[1])
print("Column 3 = ", a[:,2]) 
print("2nd element of 3rd row is ",a[2,1])

add = np.array([[1,2,3],
                [4,5,6]])

print(add+10)

x=np.array([1,2,3])  
y=np.array([10,20,30]) 
print(x+y)