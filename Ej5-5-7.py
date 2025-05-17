from math import * 
print("-------------------------------------------------------------")
print("DETERMINAR SI UN NÚMERO INGRESADO ES PRIMO")
print("-------------------------------------------------------------")

n=int(input("Ingresar un número: "))

i=2

for i in range(2,n):
        if n%i==0:
            print("-------------------------------------------------------------")
            print("El número ",n," no es primo")
            print("-------------------------------------------------------------")
            i=i+1

            break
        else:
            print("-------------------------------------------------------------")
            print ("El número ",n," es un número primo")
            print("-------------------------------------------------------------")
            i=i+1

            break