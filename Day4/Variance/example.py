import statistics as stat
import random 

numbList=[]
for i in range(1,19):
    numb=random.randint(1,188)  
    numbList.append(numb)

print(numbList)
print(stat.variance(numbList))