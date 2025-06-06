import math
import random
largo=int(input("Indicar la longitud del vector: "))
Vector=[]
Vector_par=[]
Vector_impar=[]
max=0
suma=0
contador_par=0
contador_impar=0
for i in range(largo):
    elemento=math.trunc(random.random()*100)
    Vector.append(int(elemento))
print ("Vector original: ",Vector)

for i in range(largo):
    elemento=Vector[i]
    if elemento % 2 ==0:
        Vector_par.append(elemento)
        contador_par=contador_par+1
    else:
        Vector_impar.append(elemento)
        contador_impar=contador_impar+1
print("Vector de pares: ",Vector_par)
print("El vector pares tiene ",contador_par," elementos")       
        
print("Vector de impares: ",Vector_impar)
print("El vector impares tiene ",contador_impar," elementos")       
    
    