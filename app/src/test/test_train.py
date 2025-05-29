import os
import subprocess

def test_model_training():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # app/src/test/
    model_path = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "artifacts", "model.pkl"))

    if os.path.exists(model_path):
        os.remove(model_path)

    env = os.environ.copy()
    env["WANDB_API_KEY"] = os.getenv("WANDB_API_KEY", "")
    env["USE_WANDB"] = "false"  # Desactiva wandb en test

    subprocess.run(["python", "app/src/train.py"], check=True, env=env)

    assert os.path.exists(model_path), f" El modelo no se generó correctamente en {model_path}"