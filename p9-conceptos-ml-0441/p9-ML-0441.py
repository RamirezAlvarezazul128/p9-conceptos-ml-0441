# Ramirez Azul NC 0441 NL 48

import pandas as pd

print(pd.__version__)  # Output: 1.5.2

print("---Caso Práctico en Código (Python + Pandas)---")

# 1. Crear un dataset de ejemplo similar a un CSV
datos = {
    "distancia_km": [2.5, 4.0, 1.2, 5.8, 3.1],
    "trafico_nivel": [1, 3, 1, 3, 2],  # 1: Bajo, 2: Medio, 3: Alto
    "edad_repartidor": [22, 35, 19, 28, 40],
    "tiempo_entrega_min": [15, 32, 10, 42, 25],  # Lo que queremos predecir
}

df = pd.DataFrame(datos)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[["distancia_km", "trafico_nivel", "edad_repartidor"]]  # Features / Entradas
y = df["tiempo_entrega_min"]  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

print("---Reto de Aprendizaje Basado en Problemas (ABP)---")

# 18. Datos correspondientes a NL 48
datos18 = {
    "distancia_km": [4.5, 2.0, 5.2, 1.7, 3.1],
    "trafico_nivel": [3, 1, 2, 3, 2],
    "edad_repartidor": [37, 26, 40, 24, 33],
    "tiempo_entrega_min": [44, 14, 40, 19, 24],
}

df = pd.DataFrame(datos18)

# 2. Separar las características (X) y el objetivo (y)
X = df[["distancia_km", "trafico_nivel", "edad_repartidor"]]
y = df["tiempo_entrega_min"]

# 3. Verificar la estructura
print("Características (X):")
print(X.head())

print("\nObjetivo (y):")
print(y.head())

print("\nprograma realizado por Ramirez Azul NC 0441 NL 48")