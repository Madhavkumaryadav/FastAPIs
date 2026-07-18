from fastapi import FastAPI 

app=FastAPI()

@app.get("customer")
def info_customer(customer_id :int):
    return {
        "Customer Id " : customer_id,
        
    }
