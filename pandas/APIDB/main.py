from fastapi import FastAPI,status,exception_handlers,APIRouter

# this where we will get the table data 
from Configration import collection     
from Database.schema import  get_All_Todo
from Database.models import Todo
app=FastAPI()
router=APIRouter()
from bson.objectid import ObjectId
from datetime import datetime

@router.get("/")
async def get_Todos():
    # get all data from the collection 
    data= collection.find()  
    return  get_All_Todo(data)


@router.post("/create")
async def create_Todo(todo:Todo):
    data=collection.insert_one(dict(todo))
    return {"status_code":200, "_id":str(data.inserted_id)}



@router.put("/{task_id}")
async def update(task_id:str , updated_task:Todo):
    try:
        id=ObjectId(task_id)
        exist_task=collection.find_one({"id":id, "is_delete":False})
        if not exist_task:
            return {"status_code":400, "message":"Id not found"}
        updated_task.updated_at=int(datetime.timestamp( datetime.now()))
        response=collection.update_one({"id":id},{"$set":dict(updated_task)})
        return {"status_code":200, "message":"Updated"}
    except Exception as e:
        pass



app.include_router(router)