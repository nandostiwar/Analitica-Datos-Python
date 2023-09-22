"""
1. Explicación
El conjunto de datos Iris es una colección ampliamente reconocida de información botánica 
que contiene 150 observaciones de plantas de iris, divididas en tres especies diferentes. 
Creado en 1988 por R.A. Pescador y donado por Michael Marshall, este conjunto de datos se ha utilizado en 
numerosas investigaciones de reconocimiento de patrones y análisis de datos. Sus características incluyen 
mediciones numéricas de la longitud y el ancho de los sépalos y pétalos de las plantas, junto con la etiqueta de clase
que indica la especie. Un aspecto destacado es que una de las especies es linealmente separable de las otras dos, lo que
lo convierte en un caso de estudio importante en la clasificación. No hay valores faltantes en los datos, y su distribución 
de clases es equitativa, con un tercio de las observaciones para cada especie.

"""
#2. importar y validar datos

import itertools
import numpy as np
import pandas as pd

# Ruta al archivo CSV (asegúrate de usar barras invertidas dobles o una barra inclinada)
DatasetName = r'.\data\iris.data'


# Carga el archivo CSV en un DataFrame de pandas
Data = pd.read_csv(DatasetName, sep=',', header=None)

# Muestra las primeras filas del DataFrame
print(Data.head(),"\n")

print(Data.describe(),"\n")


#3. Separar por clases

# Número de muestras por clase
NumSamples = Data.shape[0]

# Filtrando muestras por clase
dataClass1 = Data.loc[Data[4] == 'Iris-setosa']
dataClass2 = Data.loc[Data[4] == 'Iris-versicolor']
dataClass3 = Data.loc[Data[4] == 'Iris-virginica']

# Número de muestras por clase
NumSamplesClass1 = dataClass1.shape[0]
NumSamplesClass2 = dataClass2.shape[0]
NumSamplesClass3 = dataClass3.shape[0]


# Imprimiendo resultados
print('Número de muestras totales: ', NumSamples,"\n")

print('Número de muestras por clase 1 (Iris Setosa) : ', NumSamplesClass1, ' (', 100 * NumSamplesClass1 / NumSamples, ' %)')
print('Número de muestras por clase 2 (Iris Versicolour): ', NumSamplesClass2, ' (', 100 * NumSamplesClass2 / NumSamples, ' %)')
print('Número de muestras por clase 3 (Iris Virginica): ', NumSamplesClass3, ' (', 100 * NumSamplesClass3 / NumSamples, ' %)',"\n")



#4. Cambio de datos a tipo numpy. PARA IMPRIMIR TOCA BORRAR EL COMENTARIO Y COMILLAS DE LOS PRINT'S
DataAsNumpy = np.concatenate((dataClass1.values, dataClass2.values, dataClass3.values ), axis=0)


X = DataAsNumpy[:,0:4]
Y = DataAsNumpy[:,4]

"""print(X.shape)           Para imprimir borrar este texto y borrar comillas
print(Y.shape)    

print(X)
print(Y)"""

#5.1 max y min de cada atributo/columna

columnas_excluida_ultima = Data.iloc[:, :-1]

maximos = columnas_excluida_ultima.max()

minimos = columnas_excluida_ultima.min()

print("Valor Máximo de Cada Columna (excepto la última):")
print(maximos)

print("\nValor Mínimo de Cada Columna (excepto la última):")
print(minimos)


#5.2 Vector en linea del 3x3 apartir de la segunda clase (Versicolor)

# Obtener las filas 51, 52 y 53 de 'Data'
filas_51_52_53_versicolor = Data.iloc[50:53].copy()

# Convertir las filas seleccionadas en un vector de NumPy
vector_versicolor = filas_51_52_53_versicolor.to_numpy()
print("")
print(vector_versicolor,"\n")
