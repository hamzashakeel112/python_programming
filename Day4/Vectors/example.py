# vector are sequence of number that represent a point of direction in one space 
# python dont have vector but it can be represent in several ways
# it can be either row or column 
import numpy as np

# vector using list 
vector1=[1,3,5,9]
print(vector1[2])

vector2=[1,2,3]

# vector concatenation 
# print(vector1+vector2)

result=[vector1[i] + vector2[i] for i in range(len(vector2))]
# print(result)


# vector using Arrays

v1=np.array([1,2,4])
v2=np.array([3,5,7])

print(v1*2)
