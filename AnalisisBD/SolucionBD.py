import itertools
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

DataSetName = r"C:\Users\USUARIO\Pictures\Universidad\Semestre 4\Analítica Datos\AnalisisBD\BD_computer+hardware\machine.data "
Data = pd.read_csv(DataSetName, sep=',', header=None)
# print(Data.head())
# print("\n",Data.describe())

#Numero de clases completas
NumSamples = Data.shape[0]#Escogemos todas las filas


#Filtro muestras por clases
PRP_0_20 = Data.loc[ (Data[:][8]>=0) & (Data[:][8]<=20) ]
PRP_21_100 = Data.loc[ (Data[:][8]>=21) & (Data[:][8]<=100) ]
PRP_101_200 = Data.loc[ (Data[:][8]>=101) & (Data[:][8]<=200) ]
PRP_201_300 = Data.loc[ (Data[:][8]>=201) & (Data[:][8]<=300) ]
PRP_301_400 = Data.loc[ (Data[:][8]>=301) & (Data[:][8]<=400) ]
PRP_401_500 = Data.loc[ (Data[:][8]>=401) & (Data[:][8]<=500) ]
PRP_501_600 = Data.loc[ (Data[:][8]>=501) & (Data[:][8]<=600) ]
PRP_600 = Data.loc[ Data[:][8]>=600 ]

#Numero de muestras por clases
NumSamplesPRP1 = (PRP_0_20.shape[0])
NumSamplesPRP2 = (PRP_21_100.shape[0])
NumSamplesPRP3 = (PRP_101_200.shape[0])
NumSamplesPRP4 = (PRP_201_300.shape[0])
NumSamplesPRP5 = (PRP_301_400.shape[0])
NumSamplesPRP6 = (PRP_401_500.shape[0])
NumSamplesPRP7 = (PRP_501_600.shape[0])
NumSamplesPRP8 = (PRP_600.shape[0])

## Imprimiendo resultados
print('Número de muestras totales: ', NumSamples)
print('Número de muestras por clase 1: ',NumSamplesPRP1,' (',100*NumSamplesPRP1/NumSamples,' %)')
print('Número de muestras por clase 2: '+str(NumSamplesPRP2)+' ('+str(round(100*NumSamplesPRP2/NumSamples))+' %)')
print('Número de muestras por clase 3: '+str(NumSamplesPRP3)+' ('+str(round(100*NumSamplesPRP3/NumSamples))+' %)')
print('Número de muestras por clase 4: '+str(NumSamplesPRP4)+' ('+str(round(100*NumSamplesPRP4/NumSamples))+' %)')
print('Número de muestras por clase 5: '+str(NumSamplesPRP5)+' ('+str(round(100*NumSamplesPRP5/NumSamples))+' %)')
print('Número de muestras por clase 6: '+str(NumSamplesPRP6)+' ('+str(round(100*NumSamplesPRP6/NumSamples))+' %)')
print('Número de muestras por clase 7: '+str(NumSamplesPRP7)+' ('+str(round(100*NumSamplesPRP7/NumSamples))+' %)')
print('Número de muestras por clase 8: '+str(NumSamplesPRP8)+' ('+str(round(100*NumSamplesPRP8/NumSamples))+' %)')

## Cambio de datos a tipo numpy
DataAsNumpy = np.concatenate((PRP_0_20.values, PRP_21_100.values, PRP_101_200.values, PRP_201_300.values,
                               PRP_301_400.values, PRP_401_500.values, PRP_501_600.values, PRP_600.values), axis=0)

X = DataAsNumpy[:,1:9]
Y = DataAsNumpy[:,9]

# print(X.shape)
# print(Y.shape)

print(X)
# print(Y)

print()
a= (X[0][0])
b= (X[-1][-1])
c= eval(X[-1][0])
d= (X[0][-1])
# print(a)
# print(b)
# print(c)
# print(d)

#Promedio suma de las 4 esquinas de la variable X
lista=[a,b,c,d]
suma=0
for num in lista :
    suma += int(num) 
pmdo_4Esq=np.mean(suma)

#Sacar el promedio de la segunda fila en la variable X
#Me toco sacar el promedio de la primera pq el resto tienen variables string
w = X[0]
print(w)
sumaFila1=0
for num in w:
    sumaFila1 += int(num)
pmdo_Fila1=np.mean(sumaFila1)

#Editar la ultima fila de la variable X
X[-1] = 0
# print(X[-1])
