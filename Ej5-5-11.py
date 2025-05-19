import random
from math import *

print("-------------------------------------------------------------")
print("INGRESAR UN CONJUNTO DE NÚMEROS Y DETERMINAR CUÁNTOS DE ELLOS SON PARES")
print("-------------------------------------------------------------")

cant=int(input("¿Cuántas nñumeros querés comparar?: "))
cont=0
for i in range(cant):
    car=int(random.random()*100)
    if car%2==0:
        cont=cont+1
        print(car," es par")
    else:
        print(car)
    
print("-------------------------------------------------------------")
print("En la serie de ",cant," números hay ",cont," números pares")
print("-------------------------------------------------------------")

