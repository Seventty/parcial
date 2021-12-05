from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, Optional
from uuid import uuid4 as ID

app = FastAPI()

agenda = []

class post(BaseModel):
    id: str
    nombre: str
    telefono: str
    correo: str

@app.get('/')
def read_roof():
    return {"mensaje": "hola mundo"}

@app.get('/lista')
def list_roof():
    return agenda

@app.post('/guardar')
def save_post(post: post):
    post.id = str(ID())
    print(ID)
    agenda.append(post.dict())
    return "guardado corretamente"

@app.delete('/post{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(agenda):
        if post["id"] == post_id:

            agenda.pop(index)
            return "borrado correctamente"