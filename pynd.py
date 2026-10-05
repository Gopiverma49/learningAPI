from pydantic import BaseModel
from fastapi import FastAPI

app=FastAPI()


class loan(BaseModel):
    age:int
    name:str
    loan_amu:float
    years:int

@app.post("/predict")
def predict(application:loan):
    return {
        "name":application.name,
        "age":application.age,
        "year":application.years
    }