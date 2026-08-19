import numpy as np

# like a matrix *  for single row ar column 
# (1*9)+ (2*8)+(4*7)+(4*6)


v1= np.array([1,2,3,4])
v2=np.array([9,8,7,6])
result= v1.dot(v2)
print(result)


are=np.array([[1,3,4,5,6],[2,4,6,7,8]])
aer2=np.array([[12,13,14,15,16],[17,18,19,20,21]])
print(are.shape)
aer2.T
# print(are.dot(aer2))


#in dot product the size of col of 1st matrix/array must = to rows of 2nd matrix/array

vt1=np.array([
    [1,2,3,4,5],
    [2,4,7,2,8]
    ])
vt2=np.array([
    [1,2,3,4,5],
    [9,8,7,6,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [9,8,7,6,5]])
result = vt1.dot(vt2)
print(result)


print(len(vt1))
# the result will alwasys come with the number of rows of 1st matrix/array and column of 2nd matrix


# len(v1)  will give number of rows 
# len(v1[0])this will print the number of column

x=np.array([
    [2,3,4],
    [4,5,6],
    [8,2,3]
])
y=np.array([
    [1,3,5],
    [2,4,6],
    [9,8,5]
]
)
c=np.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
])

for i in range(len(x)):  # give number of row inside 
    for j in range(len(y[0])): #give number of column 
        for k in range(len(y)): # this will go through y matrix row 

            
            # x[i][j] this will go through row of x
        
            # y[k][j] the k will be incremented for column for y 
            c[i][j]+=x[i][k]*y[k][j]

for result in c:
    print(result)