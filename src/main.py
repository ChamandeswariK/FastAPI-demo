from fastapi import FastAPI, Path, HTTPException, Query
import json


app = FastAPI(
description="FastAPI Demo"
)

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {"message" : "Patient Management System API"}

@app.get('/about')
def about():
    return {'message': 'Fully Functional API to mange to your patient records'}


@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}', )
def view_patient(patient_id: str = Path(...,description="ID of the Patient in the DB", examples=['P001','P005'])):
    # load all patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient Not Found')

@app.get('/sort')
def sort_patients(sort_by:str = Query(..., description='Sort on the basis of hight, weight and bmi'), order: str = Query('asc', description='Sort in asc or desc order')):

    valid_feilds = ['height','weight','bmi']

    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400, detail=f'Invalid Feild select from {valid_feilds}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc or desc')

    data = load_data()

    sorted_order = True if order=='desc' else False

    sored_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sorted_order)

    return sored_data