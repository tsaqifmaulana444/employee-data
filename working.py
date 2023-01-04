from fastapi import FastAPI

app = FastAPI()

EMPLOYEE_DATABASE = ["Lee Kwan Htet", "Piotr Szczcrazscny", "Miguel Fernandes"]

@app.get('/')
def home():
    return {'message':'welcome, please open the /docs in the url'}

@app.get("/list-employees")
def list_employees():
    return {"employee" : EMPLOYEE_DATABASE}