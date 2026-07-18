from fastapi import FastAPI 
from pydantic import BaseModel 

app=FastAPI()

class LoanApplication(BaseModel):
    Age : int
    Income : float
    loan_amount : float 
    employment_year : int


@app.post("/predict")
def predict_loan(application: LoanApplication):
    
    if application.Age >18 and application.Income >= 70000 and application.employment_year >=2 :
        decision  = "Accepted"