from fastapi import FastAPI

app=FastAPI()

all_cus=[
    {"name":"gopi","city":"benga","risk":10},
    {"name":"yes","city":"odia","risk":1},
    {"name":"ram","city":"hsity","risk":18}
]


@app.get("/customer")
def cus(city:str, risk:int):
    filtered=[
        c for c in all_cus
        if c["city"]==city and c["risk"]==risk
    ]
    return {
        "result":filtered
    }


    
