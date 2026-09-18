# Analisis_del_rendimiento_academico
Este proyecto realiza un análisis de datos sobre las calificaciones de un grupo de estudiantes para identificar patrones y saber que influye en su rendimiento académico.

##Dataset
*Nombre del dataset: Students Performance in Exams
*Fuente: Kaggle
*Descripción: El datset contiene información sobre el desempeño de 1000 estudiantes en tres áreas principales (matemáticas, lectura y escritura), junto con variables sociodemográficas como género, nivel educativo de los padres, tipo de almuerzo y finalización de un curso de preparación.

##Objetivo
El objetivo principal es analizar el desempeño de los estudiantes para identificar patrones relacionados con sus resultados académicos mediante análisis estadístico y visualización de datos.

##Requisitos
Se requiere Python 3 y las siguientes dependencias, las cuales están detalladas con sus versiones en el archivo requirements.txt:
*pandas
*matplotlib
*seaborn
*numpy

##Instalacion
*Clonar el repositorio:    git clone https://github.com/DanCro21/Analisis_del_rendimiento_academico.git
*Entrar al proyecto: cd Analisis_del_rendimiento_academico
*Crear el entorno: python -m venv .venv
*Activarlo e instalar dependencias: 
source .venv/bin/activate
pip install -r requirements.txt

##Ejecucion
Para ejecutar el analisis y generar las visualizacionesen, ejecuta el siguiente comando desde la terminal:
python src/analysis.py

##Analisis realizados
*Identificacion de la materia con el promedio más alto.
*Comparacion del rendimiento entre estudiantes que tomaron o no el curso de preparacion.
*Analisis de la influencia del nivel educativo de los padres en las calificaciones.
*Analisis de rendimiento desglosado por genero.

##Resultados y conclusiones
A partir de los analisis y las visualizaciones generadas, se identifica que las matematicas representan la materia con el rendimiento más bajo a nivel general, convirtiéndose en el area principal que requiere mayor atencion y se comprobo la alta efectividad del curso de preparacion, ya que los estudiantes que lo completaron obtuvieron calificaciones superiores, logrando mas de 7 puntos de ventaja en su promedio general en comparacion con aquellos que no lo cursaron. Finalmente, se noto una marcada brecha educativa relacionada de forma directa con el nivel de estudios de los padres, los alumnos con padres que poseen estudios de posgrado muestran los promedios mas altos, superando por mas de 10 puntos a los estudiantes pertenecientes a entornos con menor nivel educativo formal.