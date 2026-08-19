import random
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg
# random value generator 

arr_rg=gen(pcg())
arr_rg.normal(size=(5,5))
print(arr_rg)


# random variable picker 
v1="variable 1"
v2="variable 2"
v3="variable 3"
v4=23
v5=1234

choises=[v1,v2,v3,v4,v5]
# print(random.choice(choises))


