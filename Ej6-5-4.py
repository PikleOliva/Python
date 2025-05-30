import math
import random

print("-------------------------------------------------------")
print("Complemento3: INTERACTUAR CON UN VECTOR A TRAVÉS DE OPCIONES")
print("-------------------------------------------------------")
#inicializar

Vector = 100*[0]
i=0
print(Vector)
#Llenar el vector con elementos de 1 a 100

tamanio=int(input("Ingresar el tamaño del vector (máx 100): "))

opcion=-1
for i in range(tamanio): 
    Vector[i].append(math.trunc(random.random()*100))

print (Vector)
 

while opcion!=0:
    print("-------------------------------------------------------")
    print("1 - Ingresar un elemento al vector")
    print("2 - Eliminar un elemento del vector")
    print("3 - Listar los elementos del vector")
    print("4 - Determinar la ocurrencia de un elemento en el vector")
    print("5 - Calcular la media y el máximo de los elementos del vector")
    print("0 - Para salir del programa")
    print("-------------------------------------------------------")
    opcion= print(input("Elegir una opción (0 para salir del programa):"))

for i in range(tamanio): 
    Vector[i]=input(random.random())*tamanio
print (Vector)
    