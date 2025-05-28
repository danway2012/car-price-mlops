import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import wandb

# 1. Cargar el dataset
df = pd.read_csv("data/CarPrice_Assignment.csv")
df.drop(columns=['car_ID'], inplace=True)
df.columns = df.columns.str.strip().str.replace(' ', '_')

# 2. Preprocesamiento mínimo basado en análisis del notebook
df['CarBrand'] = df['CarName'].apply(lambda x: x.split(' ')[0].lower())
df.drop(columns=['CarName'], inplace=True)
df['CarBrand'] = df['CarBrand'].replace({
    'maxda': 'mazda', 'porcshce': 'porsche', 'toyouta': 'toyota',
    'vokswagen': 'volkswagen', 'vw': 'volkswagen', 'Nissan': 'nissan'
})

# 3. Definir features finales basadas en RFE/VIF
features = ['curbweight', 'enginesize', 'boreratio', 'carwidth', 'horsepower',
            'CarBrand', 'fuelsystem', 'drivewheel', 'carbody', 'fueltype']
target = 'price'

# 4. Iniciar el experimento W&B (una vez ya existe `features`)
wandb.init(
    project="car-price-mlops",
    name="linear-regression-v1",
    config={
        "model_type": "LinearRegression",
        "features": features,
        "test_size": 0.2,
        "scaler": "MinMaxScaler",
        "encoder": "OneHotEncoder"
    }
)

# 5. Separar X e y
X = df[features]
y = df[target]

# 6. Separar numéricas y categóricas
numerical_cols = ['curbweight', 'enginesize', 'boreratio', 'carwidth', 'horsepower']
categorical_cols = ['CarBrand', 'fuelsystem', 'drivewheel', 'carbody', 'fueltype']

# 7. División train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Preprocesamiento
preprocessor = ColumnTransformer([
    ("num", MinMaxScaler(), numerical_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
])

# 9. Pipeline
pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("regressor", LinearRegression())
])

# 10. Entrenar
pipeline.fit(X_train, y_train)

# 11. Evaluación
r2 = pipeline.score(X_test, y_test)
print(f"R2 en test: {r2:.4f}")
wandb.log({"r2_score": r2})  # Log en W&B

# 12. Guardar modelo
os.makedirs("artifacts", exist_ok=True)
joblib.dump(pipeline, "artifacts/model.pkl")
print("✅ Modelo guardado en artifacts/model.pkl")
