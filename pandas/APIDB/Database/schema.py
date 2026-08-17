def get_todo(todo):
    return{
        "id":str(todo["_id"]),
        "title":todo["title"],
        "description":todo["description"],
        "is_complete":todo["is_complete"],
    }


def get_All_Todo(todos):
    return[get_todo(todo) for todo in todos ]