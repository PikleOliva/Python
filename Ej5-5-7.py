from math import * 
print("-------------------------------------------------------------")
print("DETERMINAR SI UN NÚMERO INGRESADO ES PRIMO")
print("-------------------------------------------------------------")

n=int(input("Ingresar un número: "))
con=0


for i in range(2,n):
        if n%i==0:
            con=con+1
   
if con==0:
    print("-------------------------------------------------------------")
    print("El número ",n," es un número primo")
    print("-------------------------------------------------------------")
else:
    print("-------------------------------------------------------------")
    print ("El número ",n," no es un número primo")
    print("-------------------------------------------------------------")
        
               