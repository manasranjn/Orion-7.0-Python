import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10]])

# print(arr1.sum())
# print(arr1[2].sum())
# print(arr2.sum())
# print(arr2[1].sum())
# print(arr2)
# print(arr2.sum(axis=0)) #column wise sum
# print(arr2.sum(axis=1)) #row wise sum

# print(np.sqrt(arr1))
# print(np.sqrt(arr1[3]))
# print(np.sqrt(arr2))

# print(np.square(arr1))
# print(np.square(arr1[3]))
# print(np.square(arr2))

arr2 = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10]])
# print(arr2[2][3]+10)
# print(arr2[2][3]-10)
# print(arr2[2][3]*10)
# print(arr2[2][3]/10)

arr3 = np.array([1,2,3,4,5])
arr4 = np.array([10,20,30,40,50])

arr5 = arr3 + arr4
# print(arr5)   

d1 = np.dot(arr3, arr4)
# print(d1)

p1 = np.power(arr4, 2)
p2 = np.power(arr4, arr3)
# print(p1)
# print(p2)

newArr = np.ravel(arr2)
# print(newArr)
newarr2 = newArr.reshape(2,6)
# print(newarr2)

# Indexing and Slicing in NumPy
# 1.One Dimensional Array
a1 = np.array([1,2,3,4,5])
# print(a1[2])
# print(a1[-1])
# print(a1[1:3])
# print(a1[2:])
# print(a1[:3])

# 2. Two Dimensional Array
a2 = np.array([[1,2,3,4], [5,6,7,8], [3,4,5,6], [7,8,9,0], [1,2,3,4], [5,6,7,8]])

# print(a2[2])
# print(a2[3][2])
# print(a2[3,2])
# print(a2[-2])
# print(a2[0:2, 2:3])
# print(a2[0:2, 2:])
# print(a2[:3, :2])

# 3. Boolean Indexing   
# a3 = a2>5
# print(a3)

# Iteration in NumPy
for i in a2:
    print(i)
    for j in i:
        print(j)