import random, math
import numpy as np

print("----------------------------------------------------")
print("CREAR Y LLENAR UNA MATRIZ")
print("----------------------------------------------------")

# Creamos una matriz vectores vacía 

Mat=[]

# Establecemos la dimensión de la matriaz. 
fila=int(input("Ingresar el número de filas de la matriz: "))
col=int(input("Ingresar el número de columnas de la matriz: "))

for i in range(fila):
    Mat. append([])
    for j in range(col):
        Mat[i].append(int(input("Mat {} {}: ".format(i+1)(j+1))))   
print (Mat)
