from fastapi import FastAPI
import uvicorn
import pickle

app = FastAPI()

@app.get("/{name}")
def hello(name):
    return {"Hello {} and welcome to this API".format(name)}


@app.get("/")
def greet():
    return {"Hello world"}

if __name__ == "__main__":
    uvicorn.run(app)
    