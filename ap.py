from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def home():
    return {"message":"api is working"}

@app.get("/about")
def about():
    return {"message":"about me"}

@app.get("/cust")
def custt(cust_id : int):
    return {
        "name": cust_id,
        "age": 56,
        "place": "janakpur"
    }



    