from fastapi import FastAPI 
import json 

def load_data():
    with open('paitents.json','r') as f:
        data=json.load(f) 
        
    return data

app=FastAPI() 



@app.get("/")
def hello():
    return {"Message":"Welcome to the Paitents Management API"}

@app.get("/view")
def view():
    data=load_data()
    return data

