from math import * 
print("-------------------------------------------------------------")
print("CALCULAR LA SUMA DE LOS n PRIMEROS TÉRMINOS DE UNA SUCESIÓN ARITMÉTICA")
print("-------------------------------------------------------------")

a1=float(input("Ingresar el primer término de la sucesión: "))
n=int(input("Ingresar el número de términos: "))
r= float(input("Ingresar la razón de la sucesion: "))

for i in range(1,n+1):

    an=a1+(i-1)*r
    print("El término Nro. ",i," es ",an)
    i=i+1
   

suma=trunc(a1+a1+(n-1)*r)*n/2

print("-------------------------------------------------------------")
print("La suma de los ",n," primeros términos de la sucesión aritmética")
print("que empieza con ",a1," y tiene razón ",r," es ",suma)
print("-------------------------------------------------------------")
