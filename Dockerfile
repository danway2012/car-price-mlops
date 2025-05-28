# Imagen base
FROM python:3.10-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar todo el contenido de app/
COPY app/ .

# Instalar dependencias desde app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto (entrenamiento)
CMD ["python", "src/train.py"]
