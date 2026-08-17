from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import json
import os

app = FastAPI()
FILE_PATH = "data.json"

class Task(BaseModel):
    title: str
    context: str

class TaskResponse(Task):
    id: int 

def read_file():
    if not os.path.exists(FILE_PATH):
        # FIX 1: Passed 'file' object into json.dump()
        with open(FILE_PATH, "w") as file:
            json.dump([], file)
        return []
        
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        # FIX 2: Corrected 'except Exception:' syntax
        except json.JSONDecodeError:
            return []

def write_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

@app.get("/tasks")
def get_task():
    return read_file()

@app.post("/create-task", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_data(new_task: Task):
    data = read_file()
    if data:
        new_id = max(item["id"] for item in data) + 1
    else:
        new_id = 1
        
    task_data = new_task.model_dump()
    task_data["id"] = new_id

    data.append(task_data)
    write_data(data)
    return {"message": "data is added", "task": task_data}