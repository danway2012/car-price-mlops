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


Run W&B (experimento lineal)	https://wandb.ai/daniel01hernando-universidad-politecnica-de-madrid/car-price-mlops/runs/ntmaov2j (tengo un problema con la cuenta me lo está solucionando el servicio técnico)

API desplegada en Azure (AppSvc)	https://car-price-hzgxesdjbye8htaw.spaincentral-01.azurewebsites.net/
