from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class UserPost(BaseModel):
    name: str
    body: str
    

@app.post("/post")
async def create_post(post: UserPost):
    return post