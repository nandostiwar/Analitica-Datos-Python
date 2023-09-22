import itertools
import numpy as np
import pandas as pd

url =r"C:\Users\Aio5\Downloads\iris\iris.data"

Data = pd.read_csv(url, sep=',', header=None)

Data.head()

print(Data)

Data.describe()

## Número de muestras por clase

NumSamples = Data.shape[0]


dataClass1 = Data.loc[Data[:][4]=="Iris-setosa"]
dataClass2 = Data.loc[Data[:][4]=="Iris-versicolor"]
dataClass3 = Data.loc[Data[:][4]=="Iris-virginica"]



NumSamplesClass1 = dataClass1.shape[0]
NumSamplesClass2 = dataClass2.shape[0]
NumSamplesClass3 = dataClass3.shape[0]

print('Número de muestras totales: ', NumSamples)
print('Número de muestras por campo 1: ',NumSamplesClass1,' (',100*NumSamplesClass1/NumSamples,' %)')
print('Número de muestras por campo 2: '+str(NumSamplesClass2)+' ('+str(round(100*NumSamplesClass2/NumSamples))+' %)')
print('Número de muestras por campo 3: '+str(NumSamplesClass3)+' ('+str(round(100*NumSamplesClass3/NumSamples))+' %)')

DataAsNumpy = np.concatenate((dataClass1.values, dataClass2.values, dataClass3.values), axis=0)

X = DataAsNumpy[:,:4]

print(X)

Y = DataAsNumpy[:,4]

#Maxismos
max_colum1 = np.max(X[:,0])
print("\n","Maximo valor de la columna 1 es: ",max_colum1)
max_colum2 = np.max(X[:,1])
print("Maximo valor de la columna 2 es: ",max_colum2)
max_colum3 = np.max(X[:,2])
print("Maximo valor de la columna 3 es: ",max_colum3)
max_colum4 = np.max(X[:,3])
print("Maximo valor de la columna 4 es: ",max_colum4,"\n")

#Minimos
min_colum1 = np.min(X[:,0])
print("Minimo valor de la columna 1 es: ",min_colum1)
min_colum2 = np.min(X[:,1])
print("Minimo valor de la columna 2 es: ",min_colum2)
min_colum3 = np.min(X[:,2])
print("Minimo valor de la columna 3 es: ",min_colum3)
min_colum4 = np.min(X[:,3])
print("Minimo valor de la columna 4 es: ",min_colum4,"\n")

vector_3x3 = dataClass2.iloc[:3, :3].values
print(vector_3x3)
