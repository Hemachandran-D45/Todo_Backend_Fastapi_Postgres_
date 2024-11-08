import sys
sys.path.append('./')  #this  is add the current directory 

from connection import db_session 
from model.sql_model import Todo
import decoders.todo as decode


#create todo
def create_todo(todo:str) -> dict:
    try:
        #creating new todo list
        req = Todo(todo) # from self.todo , instance of the Todo class
        db_session.add(req) 
        db_session.commit()
        return {
            'status': 'commit',
            'message': 'new todo added'
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }
    


# ---------------------------------------------------

#fetcching all todos 
def get_all():
    try:
        res= db_session.query(Todo).all() #query all todo entries from the databse
        docs = decode.decode_todos(res) #decode the retrieved todo data 
        return {
            'status': 'ok',
            'data': docs
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

#get all todo list

#update todo

#delete


# res = create_todo("Machine Learning with Python")
# print(res)

res = get_all()
print(res)