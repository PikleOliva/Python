from math import * 
print("-------------------------------------------------------------")
print("DETERMINAR CUÁNTOS CEROS HAY ENTRE LAS CIFRAS DE UN NÚMERO")
print("-------------------------------------------------------------")

n=int(input("Ingresar un número: "))
con=0

while n>=10:
    if n%10==0:
        con=con+1
        print(con)
        n=n//10
        print(n)
    else:
        n=n//10
        print(n)
        
if n==0:
    con=con+1
    print(con)
print("Hay ",con," ceros en el número seleccionado")

