from fastapi import FastAPI 

app = FastAPI()

customers={
    101:{"Name":"Madhav Yadav","risk":"Low","Score":0.15},
    102:{"Name":"Rakesh Yadav","risk":"Low","Score":0.15},
    103:{"Name":"Raghav Yadav","risk":"High","Score":0.89}
}


@app.get("/customer/{customer_id}")
def get_risk_level(customer_id :int):
    collect_id = list(customers.keys())
    if customer_id not in collect_id:
        return  {"Error " : f"Customer {customer_id} Not found ! "}
    else:
        profile = customers[customer_id]
        return {
            "Name":profile['Name'],
            "Risk":profile['risk'],
            "Score":profile["Score"]
            }