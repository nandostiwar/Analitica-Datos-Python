
import codeop
import itertools
import numpy as np
import pandas as pd


 
url=r"C:\Users\Valeria\Desktop\iris\iris.data"

Data = pd.read_csv(url, sep=',', header=None)

print (Data)
Data.head()

Data.describe()

NumSamples = Data.shape[0]

dataClass1 = Data.loc[Data[:][4]=="Iris-setosa"]
dataClass2 = Data.loc[Data[:][4]=="Iris-versicolor"]
dataClass3 = Data.loc[Data[:][4]=="Iris-virginica"]

NumSamplesClass1 = dataClass1.shape[0]
NumSamplesClass2 = dataClass2.shape[0]
NumSamplesClass3 = dataClass3.shape[0]

print('Número de muestras totales: ', NumSamples)
print('Número de muestras por clase 1: ',NumSamplesClass1,' (',100*NumSamplesClass1/NumSamples,' %)')
print('Número de muestras por clase 2: '+str(NumSamplesClass2)+' ('+str(round(100*NumSamplesClass2/NumSamples))+' %)')
print('Número de muestras por clase 3: '+str(NumSamplesClass3)+' ('+str(round(100*NumSamplesClass3/NumSamples))+' %)')

DataAsNumpy = np.concatenate((dataClass1.values, dataClass2.values, dataClass3.values), axis=0)

X = DataAsNumpy[:,:4]
print(X)

Y = DataAsNumpy[:,4]
print(Y)

#Max
maximo_columna0 = np.max(X[:,0])
print("maximo columna 0:",maximo_columna0)
maximo_columna1 = np.max(X[:,1])
print("maximo columna 1:",maximo_columna1)
maximo_columna2 = np.max(X[:,2])
print("maximo columna 2:",maximo_columna2)
maximo_columna3 = np.max(X[:,3])
print("maximo columna 3:",maximo_columna3)
#Min
minimo_columna0 = np.min(X[:,0])
print("minimo columna 0",minimo_columna0)
minimo_columna1 = np.min(X[:,1])
print("minimo columna 1",minimo_columna1)
minimo_columna2 = np.min(X[:,2])
print("minimo columna 2",minimo_columna2)
minimo_columna3 = np.min(X[:,3])
print("minimo columna 3",maximo_columna3)

#vector
vector_3x3 = dataClass2.iloc[:3, :3].values
print("Vector 3x3 a partir de la segunda clase 'Iris-versicolor':")
print(vector_3x3)


#El analisis de la base de datos contiene 3 clases, donde cada clase representa un tipo de planta de iris (Iris Setosa, Iris Versicolor, Iris Virginica)
#incluyen mediciones numéricas de la longitud y el ancho de los sépalos y pétalos de las plantas.
#Número de Instancias: 150 (50 en cada una de las tres clases)
#No contiene valores Faltantes 
#Número de Atributos: 4 atributos 
#Clase:
#Iris Setosa
#Iris Versicolor
#Iris Virginica