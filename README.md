# 🧠 Predicción de Precio de Coches

Este proyecto entrena un modelo de regresión lineal para predecir el precio de un coche a partir de sus características técnicas. Es el trabajo final de la asignatura **“Operacionalización de Machine Learning”**, del máster.

---

## 🎯 Objetivo

Aplicar buenas prácticas de MLOps a un proyecto ya desarrollado, incorporando:

-  Contenedorización con Docker
-  Tests automáticos con `pytest`
-  Seguimiento de experimentos con Weights & Biases (W&B)
-  CI/CD con GitHub Actions
-  Despliegue final en **Azure App Service**

---

## 🗂 Estructura del proyecto
CAR-PRICE-MLOPS/
├── .github/workflows/ # GitHub Actions CI/CD
│ └── test.yml
├── app/
│ ├── artifacts/ # Modelo entrenado (model.pkl)
│ ├── data/ # Dataset original (.csv)
│ ├── notebook/ # Notebook de análisis previo
│ ├── src/ # Código fuente: entrenamiento y API
│ │ ├── inference_api.py
│ │ └── train.py
│ ├── test/ # Tests automáticos con pytest
│ │ ├── test_invalid_input.py
│ │ ├── test_predict_api.py
│ │ └── test_train.py
│ └── ui/ # Interfaz web HTML
│ └── form.html
├── .env # Clave privada para W&B (excluida)
├── .gitignore
├── requirements.txt
├── Dockerfile
├── Dockerfile.api
├── docker-compose.yml
├── Makefile
└── README.md


---

## 💻 Instrucciones para entorno local

### 1. Clonar el repositorio

```bash
git clone https://github.com/danway2012/car-price-mlops.git
cd car-price-mlops
```

### 2. Construir imagen Docker

```bash
make build
```

### 3. Entrenar el modelo

```bash
make train
```


### 4. Lanzar API con interfaz web (en local)

```bash
make serve
```

## ENLACES PRÁCTICA

Repositorio GitHub	https://github.com/danway2012/car-price-mlops
Proyecto en W&B	https://wandb.ai/daniel01hernando-universidad-politecnica-de-madrid/car-price-mlops
Run W&B (experimento lineal)	https://wandb.ai/daniel01hernando-universidad-politecnica-de-madrid/car-price-mlops/runs/ntmaov2j
API desplegada en Azure (AppSvc)	https://car-price-api-dch-gaerdxcvbxg5cpax.westeurope-01.azurewebsites.net