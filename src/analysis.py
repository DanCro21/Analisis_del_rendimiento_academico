import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

#VISUALIZACIONES

#Configurar un estilo visual general para las gráficas
sns.set_theme(style="whitegrid")

#Distribución de los Promedios Generales
plt.figure(figsize=(10, 6))
sns.histplot(df['average_score'], bins=20, kde=True, color='#2c3e50')
plt.title('1. Distribución de los Promedios Académicos', fontsize=14)
plt.xlabel('Promedio General')
plt.ylabel('Cantidad de Estudiantes')
plt.savefig('outputs/resultados/1_distribucion_promedios.png', bbox_inches='tight')
plt.close() 

#Impacto del Curso de Preparación
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='test_preparation_course', y='average_score', palette='Set2')
plt.title('2. Rendimiento vs. Curso de Preparación', fontsize=14)
plt.xlabel('Curso de Preparación')
plt.ylabel('Promedio General')
plt.savefig('outputs/resultados/2_impacto_curso_preparacion.png', bbox_inches='tight')
plt.close()

#Nivel Educativo de los Padres
plt.figure(figsize=(12, 6))
orden = df.groupby('parental_level_of_education')['average_score'].mean().sort_values(ascending=False).index
sns.barplot(data=df, x='parental_level_of_education', y='average_score', order=orden, palette='viridis')

plt.title('3. Promedio según Nivel Educativo de los Padres', fontsize=14)
plt.xlabel('Nivel Educativo de los Padres')
plt.ylabel('Promedio General')
plt.xticks(rotation=45) 
plt.savefig('outputs/resultados/3_nivel_educativo_padres.png', bbox_inches='tight')
plt.close()