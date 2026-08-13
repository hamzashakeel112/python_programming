import os
import json

file_path = "data.json"

data = {"users": []}
if os.path.exists(file_path):
    # Read the existing file
    with open(file_path, "r") as file:
        data = json.load(file)
else:
    # Handle the missing file (e.g., set default data and create the file)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# print(data)


new_user=[{"name":"User1" , "age":34 , "email":"user@gmail.com"},
       {"name":"User2" ,"age":27, "email":"user2@gmail.com"}]

data["users"].extend(new_user)
print(data)