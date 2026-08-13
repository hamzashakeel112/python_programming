word="this is a free string"
# print(f"the data type of word is {word}")

# multiline string
quote='''this is a quote
 it can also go on next line'''


# get charactor at position 
# print(word[1])
# loop through string 
for i in word:
    print(i)


# length of an array
print(len(word))
# checking/finding  string 
txt="this is a free string "
print( "free" in txt)
# list


# slicing  of a string 
print(word[1:4])
print(word[:4])
print(word[2:])
print(word[-4:3])

# upper case
print(word.upper())
# lower case
print(word.lower())
# remove the space 
print(word.split())
# replace the string 
print(word.replace("H","r")) 
# split the string 
# this method witll split the string when it find any seperator 
print(word.split("t"))
# formate sting mean that we need to add the f'' in print to display string + variable 
print(f' this is a sting that show letter{word }')
