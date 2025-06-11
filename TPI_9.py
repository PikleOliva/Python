import math
print("----------------------------------------")
print("REGISTRO DE COMPRAS DIARIAS")
print("----------------------------------------")
limite=int(input("Cuál es el máximo que se puede gastar por día?: "))
compras=0
total=0
j=1
while total<limite:
    compras=int(input(f"Ingrese el valor de la compra Nº {j}? "))
    total=total+compras
    j=j+1
    if total>limite:
        total=total-compras
        print("------------------------------------------------")
        print("El saldo disponible no es sufieicien para esta compra")
        print("Usted lleva gastados $ ",total,". Le quedan para gastar $ ",limite-total)
        print("------------------------------------------------")     
    else:       
        print("------------------------------------------------")
        print("Usted lleva gastados $ ",total,". Le quedan para gastar $ ",limite-total)
        print("------------------------------------------------")
