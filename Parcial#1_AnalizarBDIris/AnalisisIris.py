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

DB_Iris = r"C:\Users\USUARIO\Documents\GitHub\Analitica-Datos-Python\Parcial#1_AnalizarBDIris\iris\iris.data" 
Data_Iris = pd.read_csv(DB_Iris, sep=',', header=None)
# print(Data_Iris.head())

# print(Data_Iris.max())
# print(Data_Iris.min())


#Numero de instancias totales de las clases
Num_Class = Data_Iris.shape[0]
# print(Num_Class)

#Separamos las clase (SON 3 CLASES)
Iris_Setosa = Data_Iris.loc[ (Data_Iris[4] == "Iris-setosa") ]#Clase N°1 :: Iris-setosa
#Maximos y Minimos de cada columna Clase N°1
MaxSetosa = Iris_Setosa.max()
MinSetosa = Iris_Setosa.min()
print("DATOS MAXIMOS Y MINIMOS IRIS-SETOSA")
print(MaxSetosa)
print(MinSetosa,"\n\n")

Iris_Versicolor = Data_Iris.loc[ (Data_Iris[4] == "Iris-versicolor") ]#Clase N°2 :: Iris-versicolor
#Maximos y Minimos de cada columna Clase N°2
MaxVersicolor = Iris_Versicolor.max()
MinVersicolor = Iris_Versicolor.min()
print("DATOS MAXIMOS Y MINIMOS IRIS-VERSICOLOR")
print(MaxVersicolor)
print(MinVersicolor,"\n\n")

Iris_Virginica = Data_Iris.loc[ (Data_Iris[4] == "Iris-virginica") ]#Clase N°3 :: Iris-virginica
#Maximos y Minimos de cada columna Clase N°3
MaxVirginica = Iris_Virginica.max()
MinVirginica = Iris_Virginica.min()
print("DATOS MAXIMOS Y MINIMOS IRIS-VIRGINICA")
print(MaxVirginica)
print(MinVirginica,"\n\n")

#Verificamos cantidad de instancias por clase (DEBEN SER UN TOTAL DE 150 O SEA, CADA CLASE DEBE TENER 50 INSTANCIAS)
Num_Class_IrisSetosa = (Iris_Setosa.shape[0])#Numero de instancias de la Clase N°1
Num_Class_IrisVersicolor = (Iris_Versicolor.shape[0])#Numero de instancias de la Clase N°2
Num_Class_IrisVirginica = (Iris_Virginica.shape[0])#Numero de instancias de la Clase N°3

# print(Num_Class_IrisSetosa) # =50 datos
# print(Num_Class_IrisVersicolor) # =50 datos
# print(Num_Class_IrisVirginica) # =50 datos

print("Numero de muestras totales: ", Num_Class)
print("Numero de muestras por clase Iris-Setosa: "+str(Num_Class_IrisSetosa)+"("+str(round(100*Num_Class_IrisSetosa/Num_Class))+"%)")
print("Numero de muestras por clase Iris-Setosa: "+str(Num_Class_IrisVersicolor)+"("+str(round(100*Num_Class_IrisVersicolor/Num_Class))+"%)")
print("Numero de muestras por clase Iris-Setosa: "+str(Num_Class_IrisVirginica)+"("+str(round(100*Num_Class_IrisVirginica/Num_Class))+"%)")

Data_Iris_AsNumpy = np.concatenate((Iris_Setosa.values, Iris_Versicolor.values, Iris_Virginica.values), axis=0)

X = Data_Iris_AsNumpy[:,0:4]
Y = Data_Iris_AsNumpy[:,4]

# print(X)
# print(Y)

#ACTIVIDADES:
#N°1 - VECTOR EN LINEA DEL 3X3 A PARTIR DE LA SEGUNDA CLASE (IRIS-VERSICOLOR) 
Vector3x3 = Iris_Versicolor.iloc[:3,:4]
Vector3x3 = np.concatenate((Vector3x3.values))
print( "\n\n", Vector3x3 )