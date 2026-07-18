from fastapi import FastAPI 
from pydantic import BaseModel 

app=FastAPI()

class LoanApplication(BaseModel):
    Age : int
    Income : float
    loan_amount : int 
    