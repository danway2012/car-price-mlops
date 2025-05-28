#  Predicción de Precio de Coches

Este proyecto entrena un modelo de regresión lineal para predecir el precio de coches en función de sus características. Forma parte de la práctica final de la asignatura **“MLOps”** del máster.

---

##  Objetivo

Aplicar buenas prácticas de MLOps a un proyecto de ML, incluyendo:

-  Contenedorización con Docker
-  Tests automáticos con Pytest
-  Seguimiento de experimentos con Weights & Biases (W&B)
-  Despliegue en Azure (App Service)
-  CI/CD automatizado con GitHub Actions

---

## Estructura del proyecto

CAR-PRICE-MLOPS/
├── .github/workflows/         # Workflow de CI/CD
│   └── test.yml
├── app/
│   ├── artifacts/             # Modelo entrenado (.pkl)
│   ├── data/                  # Dataset original
│   ├── notebook/              # Notebook original (opcional)
│   ├── src/                   # Código fuente de API + entrenamiento
│   │   ├── inference_api.py
│   │   └── train.py
│   ├── test/                  # Tests unitarios e integración
│   │   ├── test_invalid_input.py
│   │   ├── test_predict_api.py
│   │   └── test_train.py
│   └── ui/                    # Interfaz web HTML
│       └── form.html
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── README.md

---

##  Instrucciones para entorno local

### 1. Clonar el repositorio

```bash
git clone https://github.com/danielcuellar/car-price-mlops.git
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

### 4. Lanzar API con interfaz web

```bash
make serve
```

## Acceso a interfaz

http://localhost:8000
