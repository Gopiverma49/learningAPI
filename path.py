from fastapi import FastAPI

app=FastAPI()

customer_risk_pro={
    101:{"name":"gopi","risk":10},
    102:{"name":"iyan","risk":14},
    103:{"name":"ritk","risk":19}
}




@app.get("/customer/{cust_id}")
def custtm(cust_id:int):
    if cust_id not in customer_risk_pro:
        return {"error":"profile not found"}
    pro=customer_risk_pro[cust_id]
    return {
        "customer_ID":cust_id,
        "name":pro["name"],
        "risk":pro["risk"]

    }