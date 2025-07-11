import random, math
#import numpy as np

print("----------------------------------------------------")
print("SUMAR DOS VECTORES")
print("----------------------------------------------------")

# Creamos tres vectores vacíos

def cargaVector(registros):
    Vector=[]
    for i in range(registros):
        Vector.append(int((input("Ingresar el registro: "))))
    return Vector

Vect_1=[]
Vect_2=[]
Vect_Suma=[]

# Seleccionamos cuántos registros van a tener los vectores (tienen que ser iguales)
reg=int(input("Ingresar el número de elementos a introducir: "))

# Llenamos el vector de origen

Vect_1=cargaVector(reg)
Vect_2=cargaVector(reg)
Vect_Suma=[]
for i in range(reg):
    Vect_Suma.append(Vect_1[i]+Vect_2[i])
    
# Lo mostramos para ver lo que incorporamos, si hay repetidos y si está sin ordenar
print(Vect_Suma)
