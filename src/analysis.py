import pandas as pd

#Cargar el dataset
df = pd.read_csv('data/dataset.csv')

#Exploración inicial
print("Número de registros y columnas:", df.shape)
print("Tipos de datos e información general:")
df.info()