from math import * 
print("-------------------------------------------------------------")
print("DETERMINAR LOS DIVISORES ENTEROS DE UN NÚMERO")
print("-------------------------------------------------------------")

n=int(input("Ingresar un número: "))
con=0

print("-------------------------------------------------------------")
for i in range(1,n+1):
    if n%i==0:
        print("Wl número ",i," es divisor de ",n)
        print("-------------------------------------------------------------")
    
               