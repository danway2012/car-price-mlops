.PHONY: train build serve

# Construir la imagen Docker (para training o serving)
build:
	@echo "🔧 Construyendo imagen..."
	docker build -t car-price-trainer .

# Entrenar el modelo (genera artifacts/model.pkl)
train:
	@echo "🚀 Ejecutando entrenamiento..."
	docker run --rm -v ${PWD}/app/data:/app/data -v ${PWD}/app/artifacts:/app/artifacts car-price-trainer

# Servir la API con FastAPI + UI (equivalente a docker-compose up)
serve:
	@echo "🌐 Lanzando la API en http://localhost:8000 ..."
	docker-compose up --build
