from fastapi import FastAPI 


app=FastAPI()

@app.get("/")
def hello():
    return {"Message":"Welcome to the FastAPI sereis"}

@app.get("/about")
def about():
    return {'message':'Tell me something about your self'}

