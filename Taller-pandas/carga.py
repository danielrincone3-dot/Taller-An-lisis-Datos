from pathlib import Path

import pandas as pd

RAW = Path(__file__).parent / "Data" / "raw"


def cargar_datos():
    clientes = pd.read_csv(RAW / "cliente.csv")
    ventas = pd.read_csv(RAW / "ventas.csv")
    return clientes, ventas

clientes, ventas = cargar_datos()

print(ventas.shape)
print("informacion")
print(ventas.info())
print("DESCRPCION")
print(ventas.describe())

print(clientes.shape)
print("informacion")
print(clientes.info())
print("DESCRPCION")
print(clientes.describe())