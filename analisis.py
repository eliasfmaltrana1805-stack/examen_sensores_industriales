"""Analisis de sensores industriales.
"""
from pathlib import Path

import pandas as pd

RUTA_CSV = Path("data") / "sensores_industriales.csv"
RUTA_ALERTAS = Path("resultados") / "alertas.csv"
UMBRAL_C = 85

df = pd.read_csv(RUTA_CSV)

# 1. Registros y sensores distintos
print("1. Tamano del dataset")
print(f"Registros: {len(df)}")
print(f"Sensores distintos: {df['id_sensor'].nunique()}")

# 2. Temperatura promedio por planta
print("\n 2. Temperatura promedio por planta (C)")
print(df.groupby("planta")["temperatura_c"].mean().round(2).to_string())

# 3. Temperatura maxima 
max_temp = df["temperatura_c"].max()
filas_max = df[df["temperatura_c"] == max_temp]
print(f"\n 3. Temperatura maxima: {max_temp} C")
print(filas_max[["id_sensor", "fecha_hora", "planta", "temperatura_c"]].to_string(index=False))

# 4. Lecturas con alerta (> 85 C)
alertas = df[df["temperatura_c"] > UMBRAL_C]
print(f"\n 4. Lecturas con temperatura > {UMBRAL_C} C: {len(alertas)}")

# 5. Planta(s) con mas alertas 
conteo = alertas.groupby("planta").size()
print("\n 5. Alertas por planta")
print(conteo.to_string())
if len(conteo) > 0:
    maximo = conteo.max()
    ganadoras = conteo[conteo == maximo].index
    print(f"Planta(s) con mas alertas ({maximo}): {', '.join(ganadoras)}")

# 6. Exportar alertas con las columnas originales
RUTA_ALERTAS.parent.mkdir(exist_ok=True)
alertas.to_csv(RUTA_ALERTAS, index=False)
print(f"\n 6. Alertas exportadas a {RUTA_ALERTAS} ({len(alertas)} filas)")
