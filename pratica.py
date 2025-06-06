import math
import random
largo=7
Vector=[]
max=0
suma=0
contador=0
i=0
for i in range(largo):
    elemento=math.trunc(random.random()*100)
    Vector.append(int(elemento))
print (Vector)

for i in range(largo):
    termino=Vector[i]
    suma=suma+termino
    contador= contador +1
    if termino > max:
        max=termino
print ("la suma es ",suma)
print ("La media es {:.2f}".format(suma/contador))
print("El máximo es ",max)
