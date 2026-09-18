import pandas as pd

#Cargar el dataset
df = pd.read_csv('data/dataset.csv')

#Exploración inicial
print("Número de registros y columnas:", df.shape)
print("Tipos de datos e información general:")
df.info()

#Estandarizar nombres de variables (reemplazar espacios por guiones bajos)
df.columns = df.columns.str.replace(' ', '_').str.replace('/', '_')

#Revisar valores faltantes y duplicados
print("Valores nulos por columna:\n", df.isnull().sum())
print("Registros duplicados:", df.duplicated().sum())

#Eliminar duplicados en caso de existir
df = df.drop_duplicates()