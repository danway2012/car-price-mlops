import requests
import subprocess
import time

def test_invalid_input():
    # Lanzar la API temporalmente
    process = subprocess.Popen(
        ["uvicorn", "app.src.inference_api:app", "--port", "8002"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)

    try:
        payload = {
            "carbody": "sedan"  # falta todo lo demás
        }

        res = requests.post("http://localhost:8002/predict", json=payload)
        assert res.status_code == 422
    finally:
        process.terminate()
