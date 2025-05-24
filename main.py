from fastapi import FastAPI, HTTPException
from models import User
from typing import List

app = FastAPI()
users = []
user_id_counter = 1

@app.post("/users", status_code=201)
def create_user(user: User):
    global user_id_counter
    user.id = user_id_counter
    users.append(user)
    user_id_counter += 1
    return user

@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")