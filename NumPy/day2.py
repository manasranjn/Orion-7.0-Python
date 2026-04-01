import numpy as np

a =[1,2,3,4,5] #python list
x = np.array([1,2,3,4,5])
# print(x.dtype)

b = np.array([[1,2,3,4], [5,6,7,8], [3,4,5,6], [7,8,9,0], [1,2,3,4], [5,6,7,8]])

# print(b)
# print(x[3])
# print(b[2])
# print(b[2][2])
# print(b[2,1])
# print(x[-2])
# print(b[-1])
# print(b[-1][-2])
# print(b.shape)# (6,4) 6 rows and 4 columns
# print(b.size)
# print(x.size)
# print(len(b))
# print(len(x))
# print(b.itemsize)

x = np.zeros(10)
# print(x)

y = np.ones(10)
# print(y)

z = np.empty(4)
# print(z)

z = np.empty((3, 4))
# print(z)

a1 = np.arange(10)
# print(a1)
a2 = np.arange(3,10)
# print(a2)
a3 = np.arange(1,10, 2)
# print(a3)


# print(b)
# print(b.shape)
b1 = b.reshape(4,6)
# print(b1)
# b2 = b.reshape(8,3)
# print(b2)
b3 = b.reshape(12,2)
# b3 = b.reshape(2,12)
# print(b3)

l1 = np.linspace(1,10, 12)
print(l1)
print(b.min())
print(b.max())