from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

student={
    "s01":{"name":"gopi","marks":67,"grade":"A"},
    "s02":{"name":"davis","marks":78,"grade":"A"},
    "s03":{"name":"chirs","marks":69,"grade":"A"}
}

class input_sch(BaseModel):
    student_id : str
    marks : int
    grade : str



@app.get("/student/{student_id}")
def stud_id(student_id: str):
    if student_id not in student:
        raise HTTPException(
            status_code=404,
            detail="ID doenst exist"
        )

    return student[student_id]

@app.post("/submit")
def sub(submission : input_sch):
    #error1 id not found
    if submission.student_id not in student:
        raise HTTPException(
            status_code=404,
            detail="ID doenst exist"
        )
    #error2 out of range
    if submission.marks <0 or submission.marks >100:
        raise HTTPException(
            status_code=400,
            detail={
                "error":"input range isnt valid",
                "marks_entered":submission.marks,
                "valid":"enter between 0 and 100"
            }
        )

    student[submission.student_id]["marks"]=submission.marks

    return {
        "message":"marks updated successfully",
        "Updated record": student[submission.student_id]
    }