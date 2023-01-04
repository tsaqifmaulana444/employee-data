import random
import os
import json
from fastapi import FastAPI, HTTPException

app = FastAPI()

EMPLOYEE_FILE = "employee.json"
EMPLOYEE_DATABASE = ["Lee Kwan Htet", "Piotr Szczcrazscny", "Miguel Fernandes", "Wazni Mouruba"]

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
async def add_employee (employee: str):
    EMPLOYEE_DATABASE.append(employee)
    with open(EMPLOYEE_FILE, "w", encoding="UTF-8") as F:
        json.dump(EMPLOYEE_DATABASE, F)      
    return {"message" : f"{employee} successfully inserted"}