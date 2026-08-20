# flattening of nested data mean converty herarichy in single table and display it 
# it like a multiple table with retional data but we want the result to show in single table

# let say we have a list or a 3d array/matrix but we want to display it in a singlw row and table

import numpy as np
matrix=[    [1,2,3,4,5],
            [6,7,8,9,10]
        ]


list_item=[item for numb in matrix for item in numb]

# the numb here will loop through matrix but the item will store every number like append and then store it list_item 
print(matrix)
print(list_item)


# example 2

folder_content= ["documents",
                    ["Image1.png","Image2.png"],
                    ["video4mp4" ,["subfolderFile.txt"]]
                ]

def extract_file(item):
    flat_file=[]
    for element in item:
        if isinstance(element,list):  #isinstance checks whether an item is another list or a regular string otherwise it is use to check datatype.
            flat_file.extend(extract_file(element))
        else:
            flat_file.append(element)
    return flat_file
# print(extract_file(folder_content))


# example 3
classroom=[
    {"Class 1":["S1","S2","S3","S4"]},
    {"Class2":["s5","S6","S7","S8"]},
    {"Class3":["s9","S10","S11","S12"]},
 
]

# all_class=[classes for key,item in classroom.items() for classes in item]
formated_class=[
    f"{class_name} {', '.join(students)}"
    for class_dict in classroom
    for class_name,students in class_dict.items()
]
print(formated_class)
def extract(item):
    list_item=[]
    for element in item:
        if isinstance(element,dict):
            list_item.extend(extract(element))
        elif isinstance(element,list):
            list_item.extend(extract(element))
        # elif isinstance(element,item):
        #     list_item.extend(extract(element))
        else:
            list_item.append(element)
    return list_item

# print(extract(classroom))