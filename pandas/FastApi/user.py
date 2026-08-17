from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel 
from typing import List,Optional

from pymongo import MongoClient



uri = "mongodb+srv://hamzashakeel_db_user:<db_password>@cluster0.kpci5gc.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)
db = client.test

# Test connection
print(client.list_database_names())


app=FastAPI(title="JSON Data API")

class UserSchema(BaseModel):
    name:str
    email:str
    contact:str
    address:str


class UserId(UserSchema):
    id:int



# List
db_user:List[dict]=[
    {
        "id":1,
        "name":"John Doe",
        "email":"user1@gmail.com",
        "address":"123 Main St, Cityville",
        "contact":"123-456-7890"
    }
    ,
    {
        "id":2,
        "name":"Jane Smith",
        "email":"user2@gmail.com",
        "address":"456 Oak Ave, Townsville",
        "contact":"098-765-4321"
    }

]
id_counter=3
# get API
# @app.get("/users",response_model=List[UserId])
# def get_all_users():
#     return db_user

# @app.get("/users",response_model=List[UserId])
# def get_users():
#     return db_user




# @app.get("/users", response_model=List[UserId])
# def get_Users():
#     return db_user

@app.get("/users",response_model=List[UserId])
def get_users():
    return db_user


# read item by ID
# @app.get("/user/{user_id}",response_model=UserId)
# def get_user(user_id:int):
#     for user in db_user:
#         if user["id"]==user_id:
#             return user
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


# @app.get("/user/{user_id}", response_model=UserId)
# def get_by_id(user_id:int):
#     for user in db_user:
#         if user["id"]==user_id:
#             return user
#     raise HTTPException(status_code=status.http_404_NOT_FOUND, detail=f"User with ID {user_id} not found", detail=f'User with ID {user_id} not found') 

# @app.get("user/{user_id}",
#          response_model=UserId)
# def get_userId(user_id:int):
#     for user in db_user:
#         if user["id"]==user_id:
#             return user
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")

# @app.get("/user/{user_id}", response_model=UserId)
# def get_userId(user_id:int):
#     for user in db_user:
#         if user["id"]==user_id:
#             return user
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")

# @app.get("/user/{user_id}",response_model=UserId)
# def get_userId(user_id:int):
#     for user in db_user:
#         if user["id"]==user_id:
#             return user
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f'User with Id{user_id} not found'
#     )
   

@app.get('/user/{user_id}', response_model=UserId)
def get_user(user_id:int):
    for user in db_user:
        if user["id"]==user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f" User ID{user_id} not found"
    )

# @app.post("/user",response_model=UserId,
#           status_code=status.HTTP_201_CREATED)
# def create_user(user:UserSchema):
#     global id_counter
#     new_user=user.model_dump()
#     new_user["id"]=id_counter
#     db_user.append(new_user)
#     id_counter+=1
#     return new_user


# @app.post("/user",resonse_model=UserId,
#           status_code=status.HTTP_201_CREATED)
# def Create_user(user:UserSchema):
#     global id_counter
#     new_user=user.model_dump()
#     new_user["id"]=id_counter
#     db_user.append(new_user)

#     id_counter+=1
#     return new_user


# @app.post("/user",response_model=UserId,
#           status_code=status.HTTP_201_CREATED)
# def create_user(user:UserSchema):
#     global id_counter
#     new_user=user.model_dump()
#     new_user["id"]=id_counter
#     db_user.append(new_user)
#     id_counter+=1
#     return new_user
# @app.post("/user", response_model=UserId,
#           status_code=status.HTTP_201_CREATED)
# def create_user(user:UserSchema):
#     global id_counter
#     new_user=user.model_dump()
#     new_user["id"]=id_counter
#     db_user.append(new_user)
#     id_counter+=1
#     return new_user

# @app.get("/users",response_model=List[UserId])
# def get_user():
#     return db_user

# @app.get("/user/{user_id}", response_model=UserId)
# def get_userId(user_id:int):
#     for user in db_user:
#         if user["is"] == user_id:
#             return user
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f'user Id {user_id} not found'
#     )


# @app.post("/user", response_model=UserId,
#           status_code=status.HTTP_201_CREATED)
# def create_user(user:UserSchema):
#     global id_counter
#     new_user=user.model_dump()
#     new_user["id"]=id_counter
#     db_user.append(new_user)
#     id_counter+=1
# #     return new_user


# @app.put("/user/{user_id}",response_model=UserId)
# def update_user(user_id:int, updated_user:UserSchema):
#     for index,user in enumerate(db_user):
#         if user["id"]==user_id:
#             new_data=updated_user.model_dump()
#             new_data["id"]=user_id
#             db_user[index]=new_data
#             return new_data
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"User with ID {user_id} not found"
#     )


# @app.put("/user/{user_id}", response_model=UserId)
# def update_user(user:UserSchema, user_id:int):
#     for index,user in enumerate(db_user):
#         if user["id"]==user_id:
#             new_data=user.model_dump()
#             new_data["id"]=user_id
#             db_user[index]=new_data
#             return new_data
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"User with ID {user_id} not found"
#     )

# @app.put("/user/{user_id}",response_model=UserId)
# def update_user(user_id:int, user:UserSchema):
#     for index,user in enumerate(db_user):
#         if user["id"]==user_id:
#             new_data=user.model_dump()
#             new_data["id"]=user_id
#             db_user[index]=new_data
#             return new_data


# @app.put("/user/{user_id}",response_model=UserId)
# def update_user(user_id:int, user:UserSchema):
#     for index, user in enumerate(db_user):
#         if user["id"]==user_id:
#             new_data=user.model_dump()
#             new_data["id"]=user_id
#             db_user[index]=new_data
#             return new_data

# @app.put("/user/{user_id}",response_model=UserId)
# def update_user(userid:int,user:UserSchema):
#     for index, user in enumerate(db_user):
#         if user["id"]==userid:
#             new_data=user.model_dump()
#             new_data["id"]=userid
#             db_user[index]=new_data 
#             return new_data


@app.get("/users", response_model=UserId)
def get_user():
    return db_user


@app.get("/user/{user_id}", response_model=UserId)
def user_by_id(user_id{int}):
    for user in db_user:
        if user["id"]==user_id:
            return user
    raise HTTPException( status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")
@app.post("/user_create",
          response_model=UserId,
          status_code=status.HTTP_201_CREATED)
def Create_user(id:int,user:UserSchema):
    global id_counter
    new_data=user.model_dump()
    new_data["id"]=id_counter
    db_user.append(new_data)
    id_counter+=1
    return new_data

@app.put("/user/{user_id}"
         response_code=UserId)
def update_User(id:int,user:UserSchema):
    for index, user in enumerate(db_user):
        if user["id"]==id:
            new_data=user.model_dump()
            new_data["id"]=id
            # replace item at that index with the new data
            db_user[index]=new_data
            return new_data
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID {id} not found"
    )