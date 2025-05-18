from math import * 
print("-------------------------------------------------------------")
print("DETERMINAR CUÁNTOS CEROS HAY ENTRE LAS CIFRAS DE UN NÚMERO")
print("-------------------------------------------------------------")

n=int(input("Ingresar un número: "))
con=0

while n>10:
    if n%10==0:
        con=con+1
        n=n//10
        
if n==0:
    con=con+1
print("Hay ",con," ceros en el número seleccionado")

