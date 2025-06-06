import math
import random
largo=int(input("Indicar la longitud del vector: "))
Vector=[]
for i in range(largo):
    elemento=input("Ingresar nombre de animal: ")
    Vector.append(elemento)
print ("Vector original: ",Vector)
nombre=input("Ingresar el nombre del animal buscado: ")
for i in range(largo):
    if nombre in Vector:
        if i==0:
            print("A la derecha de ",nombre," está ",Vector[i+1])
        elif i==largo-1:
            print("A la izquierda de ",nombre," está ",Vector[i-1])
        else:
            print("A la izquierda de ",nombre," está ",Vector[i-1]," y a la derecha ",Vector[i+1])
            

