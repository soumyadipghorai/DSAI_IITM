from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title='Iris Prediction API')

model = joblib.load('model.joblib')

class IrisInput(BaseModel): 
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get('/')
def read_root():
    return {'message': 'Welcome to the Iris Prediction API!'}

@app.post('/predict')
def predict(iris_input: IrisInput):
    input_data = np.array([[iris_input.sepal_length, iris_input.sepal_width, iris_input.petal_length, iris_input.petal_width]])
    prediction = model.predict(input_data)
    return {'predicted_class': int(prediction[0])}

@app.post('/predict_pandas')
def predict_pandas(data: IrisInput):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)[0]
    return {'predicted_class': prediction}