# ndim will give dimension of array
# shape will give number of rows and column
# how to get 2d array to 1d array flatten 
# reshape will convert 1d to 3d we can also give parameter to this function

import numpy as np
from numpy import *
arr=np.array([[2,3,4,5,6,4],[4,5,6,7,8,8]])
# print(arr.ndim)
# print(arr.flatten())  # give one 1d array from any dimension
# print(arr.reshape(2,2,3))


# creating matrix
m=matrix('1 2 3 ; 4 5 6; 7 8 9')
# print(m)
# get diognal value
print(m.diagonal())
# to print min min()
# to print max max()
m1=matrix('1 3 5 ; 2 4 6; 8 9 10')
m2=matrix('9 7 5 ; 6 4 2; 1 2 4')
#  add 2 matix
# print (m1+m2)


# multiply by row with col the 1 col and 1 row ans come 
print(m1*m2)
# Transpose
m1.T
print(m1.T)

print(m1@m2)
