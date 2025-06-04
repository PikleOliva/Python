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

suma=sum(Vector)
print (suma)
prome=suma/largo
print(prome)

ordenado=Vector.sort()
print(ordenado)

reducido=Vector.pop()
print (reducido)
