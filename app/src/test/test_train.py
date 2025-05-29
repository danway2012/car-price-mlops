import os
import subprocess

def test_model_training():
    # Eliminar el modelo si ya existe
    model_path = "app/artifacts/model.pkl"
    if os.path.exists(model_path):
        os.remove(model_path)

    # Ejecutar entrenamiento
    subprocess.run(["python", "app/src/train.py"], check=True)

    # Verificar que se ha generado el modelo
    assert os.path.exists(model_path), "El modelo no se generó correctamente"
