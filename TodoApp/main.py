from fastapi import FastAPI
import models
from database import engine
from Routers import auth,Todos
app=FastAPI(title="FastAPI: TodoApp")
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(Todos.router)

