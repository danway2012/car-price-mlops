from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI()

# Cargar el modelo
model_path = os.path.join(os.path.dirname(__file__), "../artifacts/model.pkl")
model = joblib.load(model_path)

# Definir el modelo de entrada
class CarInput(BaseModel):
    curbweight: float
    enginesize: float
    boreratio: float
    carwidth: float
    horsepower: float
    CarBrand: str
    fuelsystem: str
    drivewheel: str
    carbody: str
    fueltype: str

# Endpoint principal de predicción
@app.post("/predict")
def predict_price(input_data: CarInput):
    input_df = pd.DataFrame([input_data.dict()])
    prediction = model.predict(input_df)[0]
    return {"predicted_price": round(prediction, 2)}

# Servir archivos estáticos (HTML UI)
app.mount("/ui", StaticFiles(directory="ui"), name="ui")

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    with open(os.path.join("ui", "form.html"), encoding="utf-8") as f:
        return f.read()
