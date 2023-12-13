# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()
origins = [

"http://localhost.tiangolo.com",

"https://localhost.tiangolo.com",

"http://localhost",

"http://localhost:8080",

"http://localhost:3000",
"http://127.0.0.1:8000",

]

app.add_middleware(

CORSMiddleware,

allow_origins=origins,

allow_credentials=True,

allow_methods=["*"],

allow_headers=["*"],

)
predictive_model = pickle.load(open('model.sav', 'rb'))
class model_input(BaseModel):
    current: float
    voltage: float
    temperature: float
    humidity: float
    vibration: float
    
predictive_model = pickle.load(open('model.sav', 'rb'))

@app.post('/prediction')
def pred(data : model_input):
    print(data.dict())
    input_list = [[
        data.current,
        data.voltage,
        data.temperature,
        data.humidity,
        data.vibration
        ]]
    result = predictive_model.predict(input_list)
    if result[0] == 0:
        return {
            "data":"Maintenance required"
            }
    else:
        return {
            "data":"No maintenance required"
            }
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    