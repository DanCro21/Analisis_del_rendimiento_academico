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

#Crear la clasificación del rendimiento académico
#Criterios definidos: Alto (>= 80), Medio (60 - 79), Bajo (< 60)
def clasificar_rendimiento(score):
    if score >= 80:
        return 'Alto'
    elif score >= 60:
        return 'Medio'
    else:
        return 'Bajo'

df['rendimiento_categoria'] = df['average_score'].apply(clasificar_rendimiento)

#Estadísticas descriptivas de las variables numéricas y categóricas
print("Estadisticas Descriptivas")
print(df[['math_score', 'reading_score', 'writing_score', 'average_score']].describe())
print("\n--- Conteo por categoria de rendimiento ---")
print(df['rendimiento_categoria'].value_counts())

#Análisis
print("\nAnalisis 1: Promedio mas alto por area")
print(df[['math_score', 'reading_score', 'writing_score']].mean())

print("\nAnalisis 2: Impacto del curso de preparacian")
print(df.groupby('test_preparation_course')['average_score'].mean())

print("\nAnalisis 3: Diferencias según el nivel educativo de los padres")
print(df.groupby('parental_level_of_education')['average_score'].mean().sort_values(ascending=False))

print("\nAnalisis 4: Rendimiento por grupos (Genero)")
print(df.groupby('gender')[['math_score', 'reading_score', 'writing_score', 'average_score']].mean())