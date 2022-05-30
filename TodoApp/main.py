from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from pydantic import BaseModel, Field
from typing import Optional

app=FastAPI(title="FastAPI: TodoApp")
models.Base.metadata.create_all(bind=engine)

def getDB():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

class Todo(BaseModel):
    title:str
    description:Optional[str]
    priority:int=Field(gt=0,lt=6,description="Priority must be between 1-5")
    complete:bool

@app.post("/")
async def create_todo(todo:Todo, db:Session = Depends(getDB)):
    todo_model=models.Todos()
    todo_model.title=todo.title
    todo_model.description=todo.description
    todo_model.priority=todo.priority
    todo_model.complete=todo.complete
    db.add(todo_model)
    db.commit()
    return successful_response(201)
        
@app.put("/{todo_id}")
async def update_todo(todo_id:int,todo:Todo,db:Session=Depends(getDB)):
    todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).first()
    if todo_model is None:
        raise HttpException()
    todo_model.title=todo.title
    todo_model.description=todo.description
    todo_model.priority=todo.priority
    todo_model.complete=todo.complete
    
    db.add(todo_model)
    db.commit()
    return successful_response(200)

@app.delete("/{todo_id}")
async def delete_todo(todo_id:int,db:Session=Depends(getDB)):
    todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).first()
    if todo_model is None:
        raise HTTPException()
    db.query(models.Todos).filter(models.Todos.id==todo_id).delete()
    db.commit()
    return successful_response(200) 
    
@app.get("/")
async def read_all(db:Session=Depends(getDB)):
    return db.query(models.Todos).all()

@app.get("/toto/{todo_id}")
async def read_todo(todo_id:int,db:Session=Depends(getDB)):
    todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HttpException()
def HttpException():
    return HTTPException(status_code=404,detail="Todo not found") 
def successful_response(status_code:int):
    return {"Status":status_code,"Transaction":"Successful"}