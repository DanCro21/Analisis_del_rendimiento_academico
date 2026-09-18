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

#Crear nueva variable 'average_score'
df['average_score'] = df[['math_score', 'reading_score', 'writing_score']].mean(axis=1)

#Crear clasificación del rendimiento académico (Criterios: Alto >= 80, Medio 60-79, Bajo < 60)
def clasificar_rendimiento(score):
    if score >= 80:
        return 'Alto'
    elif score >= 60:
        return 'Medio'
    else:
        return 'Bajo'

df['rendimiento_categoria'] = df['average_score'].apply(clasificar_rendimiento)

#Estadísticas descriptivas de las variables numéricas
print(df[['math_score', 'reading_score', 'writing_score', 'average_score']].describe())
print("\nConteo por categoría de rendimiento:\n", df['rendimiento_categoria'].value_counts())