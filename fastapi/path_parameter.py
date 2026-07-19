from fastapi import FastAPI 

app = FastAPI()

customer_detail={
    101:{"Name":"Madhav Yadav","risk":"Low","Score":0.15},
    102:{"Name":"Rakesh Yadav","risk":"Low","Score":0.15},
    103:{"Name":"Raghav Yadav","risk":"High","Score":0.89}
    
}

@app.get("/customer/{customer_id}")
def customer_risk_level(customer_id : int):
    profile=customer_detail[customer_id]
    id = customer_detail.keys()
    id=list(id)
    if customer_id not in id:
        return {"Error":f"Customer {customer_id} Not fount ! "}
    else:
        return {
            "Customer id ": customer_id,
            "Name ":profile["Name"],
            "Risk Level": profile["risk"],
            "Score ":profile["Score"]
        }
        