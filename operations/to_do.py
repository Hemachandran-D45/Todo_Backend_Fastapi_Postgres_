import sys
sys.path.append('./')

from connection import db_session
from model.sql_model import Todo
import decoders.todo as decode


#create todo
def create_todo(todo:str) -> dict:
    try:
        req = Todo(todo) # from self.todo
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
def get_all():
    try:
        res= db_session.query(Todo).all()
        docs = decode.decode_todos(res)
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