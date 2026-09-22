import numpy as np

print(np.__version__)

arr1d = np.array([1,2,3,4,5])
print(arr1d)

arr2d = np.array([
    [1,2],
    [3,4]
   ])
print(arr2d)
print(type(arr1d))
print(type(arr2d))

## check python datatypes
l = list()
print(type(l))

s = set()
print(type(s))

l1= [1,2,3]
print(type(l1))

s1 = {1,2,3}
print(type(s1))

l11 = list([1,2,3])
print(l11)
print(type(l11))

######################
# built in methods
######################

# 1. zeros
z1 = np.zeros((5,))
print(f'z1 :: {z1}')

z11 = np.zeros(shape= (2,3),dtype = np.int8)
print(f'z11 :: {z11}')

# 2.ones
o1 = np.ones(shape=(2,3),dtype = np.int8)
print(f'o1 : {o1}')

# 3. own value

f1 = np.full(shape=(3,3),fill_value=99)
print(f'f1 :: {f1}')

f2 = np.full(shape=(2,3),fill_value='anek')
print(f'f2 : {f2}')

# 4. arange
a1 = np.arange(start=1,stop=10,step=1)
print(f'arange a1 : {a1}')

a11 = np.arange(1,11,1)
print(f'arange a11 :: {a11}')

a111 = np.arange(1,6)
print(f'arage a111 : {a111}')

m1 = np.arange(-5,1,2)
print(f'minus :: {m1}')

# 3. linspace
# (20 - 10)/4 = 10/4 = 2.5 => 12.5,15.0,17.5,20
ls = np.linspace(start=1,stop=10,num=4)
print(f'linspace : {ls}')

ls1 = np.linspace(start=10,stop=20,num=4)
print(f'linspace : {ls1}')

ls11 = np.linspace(start=1,stop=10,num=5)
print(f'linspace : {ls11}')
print(ls11.dtype)

# size
ar1 = np.arange(1,100,step=40)
print(ar1.itemsize)
print(ar1.dtype)
print(ar1.shape)


print(ar1.nbytes)

# resize
a1 = np.array([1,2,3,4,5,6])
print(f'a1 size :: {a1.size}')
print(f'ndim a1 :: {a1.ndim}')

rs1 = a1.reshape((2,3))
print(f'reshape to 2x3 : \n{rs1}')

rs2 = a1.reshape((1,2,3))
print(f'reshape 1x2x3 : \n{rs2}')


t1 = np.arange(start=1,stop=13,step=1)
print(f't1 : {t1}')
tres1 = t1.reshape((3,4))
print(f'reshaping to 3x4  \n{tres1}')

# unknown dimension -1

# flatten

f1 = tres1.flatten()
print(f'faltten f1 : {f1}')

# indexing & slicing

sl1 = np.array([10,20,30,40,50,60])
print(f'indexing {sl1[-1]}')

# 2d array
#         1st ele  2nd ele   3rd ele of simple array
arr2d = np.array([
          [1,2,3],
          [4,5,6],
          [7,8,9]
          ])
print(f'arr2d : \n {arr2d.ndim}')

arr3d = np.array([
    [
        [1,2,3],[3,4,5],[6,7,8]
     ] ,
    [
        [1, 2, 3], [3, 4, 5], [6, 7, 8]
    ] ,
    [
        [1, 2, 3], [3, 4, 5], [6, 7, 8]
    ]
])
print(f'arr3d dimensions : \n {arr3d.ndim}')
print(f'arr3d shape : \n {arr3d.shape}')



