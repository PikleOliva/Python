import math
import random

print("-------------------------------------------------------")
print("Complemento3: INTERACTUAR CON UN VECTOR A TRAVÉS DE OPCIONES")
print("-------------------------------------------------------")
#inicializar

#Llenar el vector con elementos de 1 a 100

tamanio=int(input("Ingresar el tamaño del vector (máx 100): "))
Vector = tamanio * [0]
print (Vector)
i=0

for i in range(tamanio): 
   Vector[i]= int(math.trunc(random.random()*100))
    
print (Vector)
opcion=-1

print("-----------------------------------")
print("          M E N Ú    ")
print("-----------------------------------")
print("")
print("1 - Sustituir un elemento al vector")
print("2 - Eliminar un elemento del vector")
print("3 - Listar el contenido del vector")
print("4 - Determinar la repitencia de un elemento dal vector")
print("5 - Calcular la media y el máximo de un vector")
print("")
print("-----------------------------------")
opcion=int(int(input("Ingresar la opción elegida (0 para salir): ")))

if opcion == 1:
    i=int(input("Qué registro del vector desea ingresar: "))-1
    if i<tamanio:
        elemento=int(input("Qué valor desea asignarle al elemento: "))
        Vector[i]=elemento
        print (Vector)
    else:
        print("El máximo de registro del vector es de ",tamanio)
elif opcion == 2:
    print (Vector)
    num = int( input("Ingresar el número que se desea eliminar")) 
    if num > 0: 
        a = 0 
#Busca NUM en el array 
        for j in range(i): 
            if Vector[j] == num : 
                a = j
                print (Vector) 
                break 
#Re-organizar el array if a >= 0 and a <= i: for j in range(a, i-1 +1): V[j] = V[j+1] V[i] = 0 i = i - 1      