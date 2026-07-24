from pydantic import BaseModel 
from fastapi import FastAPI 


class loanapplication(BaseModel):
    Name:str
    Age:int
    Salary:float 
    Employment_year:int 
    
app = FastAPI()

@app.post("/applicant")
def approval_decision(application:loanapplication):
    approved = (
        application.Salary >=50000 and 
        application.Age >=21  and 
        application.Employment_year >2
    )
    
    return {
        "Name":application.Name,
        'Age':application.Age,
        'decision':'Aapproved' if approved else 'reject',
        'Salary':application.Salary,
        'Employment Year ':application.Employment_year,
        
    }