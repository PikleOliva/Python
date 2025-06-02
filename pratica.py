import math
import random
alto=int(input("Filas: "))
ancho=int(input("Columnas: "))
Matriz=[]
for i in range(alto):
    fila=[]
    for j in range(ancho):
        elemento= int(input(f"Elemento de la fila {i+1}: "))
        fila.append(elemento)
    Matriz.append(fila)
for fila in Matriz:
    print (fila)