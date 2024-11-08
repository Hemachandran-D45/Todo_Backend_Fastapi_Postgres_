def decode(doc) -> dict:
    return {
        '_id':doc._id,
        'title': doc.todo,
        'timstamp':doc.timestamp

    }

def decode_todos(docs)->list:
    return [
        decode(doc) for doc in docs
        
    ]