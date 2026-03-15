import numpy as np

mat1=np.array([[1,2],
               [3,4]])
mat2=np.array([[5,6],
               [7,8]])

matmul1= mat1@mat2
matmul2= np.dot(mat1,mat2)
matmul3= np.matmul(mat1,mat1)
print(matmul1)
print(matmul2)
print(matmul3)

# Matrix & Vector
v1=np.array([1,2,3])
print(v1.shape)
m1=np.array([[1],
             [2],
             [3]])
m2=np.array([[1,2,3]])
m3=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
print(m1.shape)
print(m2.shape)
print(m3.shape)

#mv1=m1@v1 will fail as (3,1)(3,) cant be multiplied.
#mv2=m2@v1 will fail as (1,3)(3,) cant be multiplied.
mv3=m3@v1 #Shape will be (3,)

print(mv3, mv3.shape)

vm1=v1@m1 #Shape will be (1,)
#vm2=v1@m2 will fail as (3,)(1,3) cant be multiplied.
vm3=v1@m3 #Shape will be (3,)

print(vm1, vm1.shape)
print(vm3, vm3.shape)
