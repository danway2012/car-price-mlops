import requests
import subprocess
import time

def test_predict_endpoint():
    # Lanzar la API temporalmente
    process = subprocess.Popen(
        ["uvicorn", "app.src.inference_api:app", "--port", "8001"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)  # Esperar a que levante

    try:
        payload = {
            "curbweight": 2337,
            "enginesize": 130,
            "boreratio": 3.47,
            "carwidth": 64.1,
            "horsepower": 111,
            "CarBrand": "toyota",
            "fuelsystem": "mpfi",
            "drivewheel": "fwd",
            "carbody": "sedan",
            "fueltype": "gas"
        }

        res = requests.post("http://localhost:8001/predict", json=payload)
        assert res.status_code == 200
        assert "predicted_price" in res.json()
    finally:
        process.terminate()
