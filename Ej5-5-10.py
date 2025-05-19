from math import * 
print("-------------------------------------------------------------")
print("DETERMINAR EL MAYOR Y EL MENOR DE UNA SERIE DE NÚMEROS")
print("-------------------------------------------------------------")

cant=int(input("Ingresar cuántos números quiere comparar: "))

n=int(input("Ingresar un número: "))
may=n
men=n

for i in range(cant-1):
    n=int(input("Ingresar un número: "))
    if n>may:
        may=n
    elif n<men:
        men=n

print("-------------------------------------------------------------")
print(may," es el número mayor de la serie")
print("-------------------------------------------------------------")
print(men, "es el número menor de la serie")
print("-------------------------------------------------------------")

