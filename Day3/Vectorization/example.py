# vectoriztion is a technique used to perform operations on entire arrays at once instead of iterating through elements using Python loops

import numpy as np
arr=np.array([20,30,45,40,50])
# vectorization
# arr* 2 mean that every element will be multiply by 2 without looping through each element of array


# c= arr*2
# print(c)


# dot product : multiply col and then add each column
arr1=np.array([[1,2,3],[7,6,5]])
arr2=np.array([[1,2,3],[4,5,9]])
# this will give error because the rule is no of col 1st = num of row of 2nd 
# d=np.dot(arr1,arr2)


d= arr1*arr2
# print(d)


# outer product : will give the matrix after multiply 2 array with 1st array
# how this work on 2d array
# the all row of 2nd array will multiply with 1st row 
# can be done on 1d array
arr3=np.array([[1,2],[5,6]])
arr4=np.array([[3,4],[7,8]])
e=np.outer(arr3,arr4)
# print(e)



# element wise product : its multiply 2 element on the same position
arr5=np.array([1,2,3])
arr6=np.array([4,5,6])
f=np.multiply(arr5,arr6)
print(f)

# @ gives consise syntax for multiply arrays 


a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

result = a @ b
print(result)