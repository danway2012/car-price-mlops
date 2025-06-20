from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI()

# Rutas seguras y absolutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.abspath(os.path.join(BASE_DIR, "..", "artifacts", "model.pkl"))
ui_dir = os.path.abspath(os.path.join(BASE_DIR, "..", "ui"))

# Cargar modelo
model = joblib.load(model_path)

# Input schema
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

# Endpoint principal
@app.post("/predict")
def predict_price(input_data: CarInput):
    input_df = pd.DataFrame([input_data.dict()])
    prediction = model.predict(input_df)[0]
    return {"predicted_price": round(prediction, 2)}

# UI
app.mount("/ui", StaticFiles(directory=ui_dir), name="ui")

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    html_path = os.path.join(ui_dir, "form.html")
    with open(html_path, encoding="utf-8") as f:
        return f.read()
