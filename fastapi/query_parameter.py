from fastapi import FastAPI 

app=FastAPI()

customers={
    101:{"Name":"Madhav Yadav","risk":"Low","City":"Delhi","Score":0.15},
    102:{"Name":"Rakesh Yadav","risk":"Low","City":"Bihar","Score":0.15},
    103:{"Name":"Raghav Yadav","risk":"High","City":"mumbai","Score":0.89},
    104:{"Name":"Madhav Yadav","risk":"Low","City":"Bihar","Score":0.15},
    105:{"Name":"Rakesh Yadav","risk":"Low","City":"Delhi","Score":0.15},
    106:{"Name":"Raghav Yadav","risk":"High","City":"Hydrabad","Score":0.89}
}

@app.get("/customer")
def get_customer_info(city:str,risk:str):
    
    filter = [
        customer for customer in customers.values()
        if customer['City'] == city and customer['risk'] == risk
    ]
    
    return {
        "city":city,
        "Risk":risk,
        "Count":len(filter),
        "Result":filter 
    }
