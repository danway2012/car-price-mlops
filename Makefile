.PHONY: train build serve


# Construir la imagen Docker (para training o serving)
build:
	@echo "Construyendo imagen..."
	docker build -t car-price-trainer .

# Entrenar el modelo (genera artifacts/model.pkl)
train:
	@echo "Ejecutando entrenamiento..."
	docker run --rm \
		--env-file .env \
		-v ${PWD}/app/data:/app/data \
		-v ${PWD}/app/artifacts:/app/artifacts \
		car-price-trainer

# Servir la API con FastAPI + UI
serve:
	@echo "Lanzando la API en http://localhost:8000 ..."
	docker compose up --build

deploy:
	@echo " Asegurando push a rama main..."
	git add .
	git commit -m " Despliegue automático a Azure desde Makefile" || echo "Nada que commitear"
	git push origin main
	@echo " Despliegue iniciado vía GitHub Actions"
