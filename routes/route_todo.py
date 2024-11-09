from fastapi import APIRouter
from model.pydantic_model import Todo
from all_routes import todo_create

todo_route = APIRouter()

#create a new todo
@todo_route.post(todo_create)
def new_todo(doc: Todo):
    return {
        'message':'Create Successfully',
        'data':doc.dict()
    }


