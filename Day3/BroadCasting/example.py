# BroadCasting is a conept of shapes in an array
# 2 condition
# 1=>size must be same 
# 2=>one of array is size of 1x1 (1 row and 1 column)
import numpy as np
# condition 1
matrix=np.array([[15,12,23],[14,15,16]])
matrix2=np.array([[5,8,3],[6,5,4]])

sum=matrix+matrix2
# print(sum)

# condition 2
arr=np.array([[3,4,5,6],[1,2,3,5]])
row=np.array([10])
print(arr*row)