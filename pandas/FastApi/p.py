# first import the fast api and other modules
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# then explain it is and fast Api 
# the app is use for endpoints and routes

app = FastAPI(title="JSON Data API without Database")

# generate a class of an item

class Person(BaseModel):
    name:str
    age:int
    email:str
    contact:str
    address:str
    job:str
    position:str

class PersonResponse(Person):
    id:int


db_persons: List[dict] = [
   { 
        "id": 1,
        "name": "Jane Smith",
        "age": 25,
        "email": "user1@gmail.com",
        "address": "456 Oak Ave",
        "contact": "098-765-4321",
        "job": "Designer",
        "position": "Team Lead"
    },
    {
        "id": 2,
        "name": "John Doe",
        "age": 30,
        "email": "user2@gmail.com",
        "address": "123 Main St",
        "contact": "123-456-7890",
        "job": "Engineer",
        "position": "Senior Developer"

    }
]



# 1st endpoint
@app.get("/persons", response_model=List[PersonResponse])
def get_all_persons():
    return db_persons



@app.get("/person/{person_id}", response_model=PersonResponse)
def get_person(person_id: int):
    for person in db_persons:
        if person["id"] == person_id:
            return person
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")


@app.post("/person",response_model=PersonResponse,
          status_code=status.HTTP_201_CREATED)
def create_person(person:Person):
    new_person=person.model_dump()
    new_person["id"]=len(db_persons)+1
    db_persons.append(new_person)
    return new_person


app.put("/person/{person_id}",
        response_model=PersonResponse)
def update_person(person_id: int, person: Person):
    for i, p in enumerate(db_persons):
        if p["id"] == person_id:
            db_persons[i] = person.model_dump()
            db_persons[i]["id"] = person_id
            return db_persons[i]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")


@app.delete("/person/{person_id}",status_code=status.HTTP_200_OK)
def delete_person(person_id:int ):
    for i,p in enumerate(db_persons):
        if p["id"]==person_id:
            remove_person=db_persons.pop(i)
            return {"message":f"Person{remove_person['name']} deleted successfully"}