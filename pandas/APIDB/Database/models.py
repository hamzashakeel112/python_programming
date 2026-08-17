from pydantic import BaseModel
from datetime import datetime
class Todo(BaseModel):
    title:str
    description:str
    is_complete:bool=False
    is_deleted:bool=False
    updated_at:int=int( datetime.timestamp( datetime.now() ))
    created_at:int=int( datetime.timestamp( datetime.now() ) )
