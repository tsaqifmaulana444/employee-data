import random
import os
import json
from typing import Optional, Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class EmployeeModel(BaseModel):
    name: str
    salary: float
    origin: str
    desc: str
    gender: Literal["Man", "Woman"]
    id: Optional[int] =  random.randint(0, 10000)

EMPLOYEE_FILE = "employees.json"

if os.path.exists(EMPLOYEE_FILE):
    with open(EMPLOYEE_FILE, "r", encoding="UTF-8") as f:
        EMPLOYEE_DATABASE = json.load(f)

@app.get('/')
async def home():
    return {'message':'welcome, please open the /docs in the url'}

@app.get("/list-employees")
async def list_employees():
    return {"employee" : EMPLOYEE_DATABASE}

@app.get("/employee-index/{index}")
async def employee_index (index: int):
    if index < 0 or index >= len(EMPLOYEE_DATABASE):
        raise HTTPException(404, f"Index {index} is out of the range {len(EMPLOYEE_DATABASE) - 1}")
    else:
        return {"employee" : EMPLOYEE_DATABASE[index]}

@app.get("/rand-employee")
async def rand_employee():
    return {"employee" : random.choice(EMPLOYEE_DATABASE)}

@app.post("/add-employee")
async def add_employee (employee: EmployeeModel):
    employee.id = random.randint(0, 10000)
    parse_employee = jsonable_encoder(employee)
    EMPLOYEE_DATABASE.append(parse_employee)
    with open(EMPLOYEE_FILE, "w", encoding="UTF-8") as F:
        json.dump(EMPLOYEE_DATABASE, F)      
    return {
        "message" : f"{employee.name} data successfully inserted", 
        "id" : employee.id
    }
    
@app.get("/get-employee")
async def get_emp_by_id(id_emp: int):
    for employee in EMPLOYEE_DATABASE:
        if employee["id"] == id_emp:
            return employee
    
    raise HTTPException(404, f"Employee with ID {id_emp} not found")