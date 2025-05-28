# Predicción de Precio de Coches 

Este proyecto entrena un modelo de regresión lineal para predecir el precio de coches en función de sus características. Forma parte de la práctica final de la asignatura **“MLOPS”** del máster.

##  Objetivo

Aplicar buenas prácticas de MLOps a un proyecto de ML, incluyendo:

- Contenedorización con Docker
- Tests automáticos
- Seguimiento de experimentos con W&B
- Despliegue en Azure
- CI/CD con GitHub Actions

---

##  Estructura del proyecto

├── app/
│ ├── src/ # Código fuente (API + entrenamiento)
│ ├── data/ # Dataset de entrada
│ ├── artifacts/ # Modelo entrenado (.pkl)
│ └── ui/ # Interfaz web HTML
├── test/ # Tests unitarios y de integración
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── README.md

---

## 🧪 Instrucciones para entorno local

### 1. Clonar el repositorio

```bash
git clone https://github.com/danielcuellar/car-price-mlops.git
cd car-price-mlops


### 2. Construir imagen Docker

make build


### 3. Entrenar el modelo

make train

### 4. Lanzar API con ui

make serve

