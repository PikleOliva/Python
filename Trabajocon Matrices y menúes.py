import math
import random

print("-------------------------------------------------------")
print("Complemento3: INTERACTUAR CON UNA MATRIZ A TRAVÉS DE OPCIONES")
print("-------------------------------------------------------")
print("")
#inicializar
filas=int(input("Ingresar cantidad de filas de la matriz (máx 100): "))
columnas=int(input("Ingresar cantidad de filas de la matriz (máx 100): "))
print("")
i=0
j=0
Matriz=[] #Estoy creando una matriz vacía
opcion=-1
print("Ingresar laopción elegida (0 para terminar)")
print("")
print("1 - Completar una matriz con elementos seleccionados")
print("2 - Completar una matriz con ceros")
print("3 - Completar una matriz con elementos aleatorios")
print("")
while opcion!=0:
    opcion=int(input("Opción seleccionada: "))
    print("")
    if opcion==1:
        for i in range(filas): 
            fila=[] 
            for j in range (columnas):
                elemento=int(input(f"Ingresar el elemento de la fila {i+1}: "))
                fila.append(elemento)
            Matriz.append(fila) 
        for fila in Matriz:
            print (fila)
    
    print("")
    if opcion==2:
        for i in range(filas):
            fila=[] 
            for j in range (columnas):
                elemento=int(0)
                fila.append(elemento)
            Matriz.append(fila) #Le agrego las filas creadas a la matriz
    
        for fila in Matriz:
            print (fila)
    if opcion==3:
        for i in range(filas):
            fila=[] 
            for j in range (columnas):
                elemento=int(math.trunc(random.random()*100))
                fila.append(elemento)
            Matriz.append(fila) #Le agrego las filas creadas a la matriz
    
        for fila in Matriz:
            print (fila)




