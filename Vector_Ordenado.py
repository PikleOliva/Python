import math
import random
largo=int(input("Indicar la longitud del vector: "))
Vector=[]
Vector1=Vector
max=0
suma=0
contador=0
i=0
for i in range(largo):
    elemento=math.trunc(random.random()*100)
    Vector.append(int(elemento))
print ("Vector original: ",Vector)
Vector1=Vector

# Se puede ordenar con el método sort() o sorted(). 
# Sorted() mantiene el vector original

Vector_ordenado=Vector.sort()
print("Vector ordenado con sort() (no sé por qué no funciona): ",Vector_ordenado)

Vector_ordenado=sorted(Vector)
print ("Vector ordenado con sorted(): ",Vector_ordenado)

#se puede ordenar manualmente

for i in range(largo): 
    for j in range(largo-1): 
        if Vector[j] > Vector[j+1]: 
            aux = Vector[j]
            Vector[j] = Vector[j+1] 
            Vector[j+1] = aux
#for i in range(largo): 
print("Vector ordenado manualmente (ascendente): ",Vector)

# Desdendente

for i in range(largo):
    for j in range(largo-1):
        if Vector1[j]<Vector1[j+1]:
            aux=Vector1[j]
            Vector1[j]=Vector1[j+1]
            Vector1[j+1]=aux
print("Vector ordenado manualmente (ascendente): ",Vector1)