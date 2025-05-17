from math import * 
print("-------------------------------------------------------------")
print("CALCULAR EL RESULTADO DE UNA SERIE DE n TÉRMINOS")
print("-------------------------------------------------------------")

n=int(input("Ingresar el valor de n: "))
suma=0
for i in range(1,n+1):
    if i%2==0:
        a1=-1/i
        print(a1)
    else:
        a1=1/i
        print(a1)
    suma=suma+a1


print("-------------------------------------------------------------")
print("La suma de los ",n," primeros términos de la sucesiónda es: ",suma)
print("-------------------------------------------------------------")
