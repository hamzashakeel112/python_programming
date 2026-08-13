fruits=["apple","mango","pineapple" ,32,44]
# print(f"the list of fruits {fruits}")


# access the specific index
# print(fruits[2])

# access the last item in the list
# print(fruits[-1])

# access list from specific index to specific
# print(fruits[2:6])

# from start to specific index
# print(fruits[:4])

# negative index the last item of the list will not be displayed
# print(fruits[-4:-1])

# print the reverse 
# print(fruits[-4:])


# check if the item is in the list
if "apple" in fruits:
    print(f"apple is in the fruits list")
else:
    print("item is not in the list")



# change the list item
fruits[1]=34
# print(fruits)

# add multiple value in the list
fruits[1:2]=["chery","bluebarry"]
# print(fruits)

# replacing one value with one letter
fruits[1:3]=["blue"]
# print(fruits)

# insert():
# insert item at specific position 
fruits.insert(2,"chery")
# print(fruits)




# append() 
# add item to list 
fruits.append("fruit1")
# print(fruits)


fruits.insert(3,"fruit2")
# print(fruits)


# extend()
# to append another list to another
numbers=[1,2,3,4,5]
fruits.extend(numbers)
# print(fruits)


#extend()
#  we can also append the tuple in a list 
tup=("x-axis","y-axis")
fruits.extend(tup)
# print(fruits)


# removing item from the list 

# remove()  we need to specify the value that is in the list 
# fruits.remove("y-axis")
# print(fruits)


# pop() 
# we need to add the index 
# no index then it will remove the last item
# fruits.pop(-1)
# print(fruits)

# del will remove the entire list and variable return error
# del fruits
# print(fruits)


# loop through each item in a list 

# for in loop
# for item in fruits:
#     print(item)


# for loop
# range(start, stop, step) dont use i inside the range 
# for i in range(0,len(fruits),1):
#     print(fruits[i])

# while loop
# in while loop i is need to be defined
# itrate=0
# while itrate< len(fruits):
#     print(fruits[itrate])
#     itrate=itrate+1

# short hand for loop 
# [print(x) for x in fruits]


items=["item-A","item-b","item-apple","item-cap"] 

newList=[x for x in items if "a" in x ]
# item-A will not be print 
#  
# print(newList)




# newlist = [expression for item in iterable if condition == True]
newList1=[x for x in fruits if isinstance(x,str) and "a" in x]
print(f' this is list 1{newList1}')




# sort() to sort a list 
# print(fruits.sort())
items.sort()
print(items)

# sort reverse 
# items.sort(reverse=True)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)


# join list 


# using 3rd list to store it
thislist1=["1","2","3"]
thislist2=["a","b","c"]
list3=[]
# list3=thislist1+thislist2
# print(list3)

# append()
list3.append(thislist1)
list3.append(thislist2)
print(list3)