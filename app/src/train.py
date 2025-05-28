import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import wandb

# 1. Cargar el dataset
df = pd.read_csv("data/CarPrice_Assignment.csv")
df.drop(columns=['car_ID'], inplace=True)
df.columns = df.columns.str.strip().str.replace(' ', '_')

# 2. Preprocesamiento mínimo
df['CarBrand'] = df['CarName'].apply(lambda x: x.split(' ')[0].lower())
df.drop(columns=['CarName'], inplace=True)
df['CarBrand'] = df['CarBrand'].replace({
    'maxda': 'mazda', 'porcshce': 'porsche', 'toyouta': 'toyota',
    'vokswagen': 'volkswagen', 'vw': 'volkswagen', 'Nissan': 'nissan'
})

# 3. Features y target
features = ['curbweight', 'enginesize', 'boreratio', 'carwidth', 'horsepower',
            'CarBrand', 'fuelsystem', 'drivewheel', 'carbody', 'fueltype']
target = 'price'

# 4. Iniciar experimento W&B
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
config = wandb.config

# 5. Preparar datos
X = df[features]
y = df[target]

numerical_cols = ['curbweight', 'enginesize', 'boreratio', 'carwidth', 'horsepower']
categorical_cols = ['CarBrand', 'fuelsystem', 'drivewheel', 'carbody', 'fueltype']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config.test_size, random_state=42)

# 6. Preprocesamiento y pipeline
preprocessor = ColumnTransformer([
    ("num", MinMaxScaler(), numerical_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
])

pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("regressor", LinearRegression())
])

# 7. Entrenar modelo
pipeline.fit(X_train, y_train)

# 8. Evaluar modelo
y_pred = pipeline.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)

print(f"✅ R2: {r2:.4f} | RMSE: {rmse:.2f} | MAE: {mae:.2f}")

# 9. Log en W&B
wandb.log({
    "r2_score": r2,
    "rmse": rmse,
    "mae": mae
})

# 10. Guardar modelo
os.makedirs("artifacts", exist_ok=True)
joblib.dump(pipeline, "artifacts/model.pkl")
print("✅ Modelo guardado en artifacts/model.pkl")
