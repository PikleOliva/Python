from random import * 
print("-------------------------------------------------------------")
print("INGRESAR 100 NUMEROS Y DECIR CUÁLES SON PARES")
print("-------------------------------------------------------------")

contador= int (0)
inicio = int(1)
fin = int(input("Ingresar la cantidad de números a contar: "))
num = int(0)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - ")
for i in range(inicio,fin+1):
    num=int(random()*100)
    if num%2==0:
        print(num," es par")
        contador=contador+1
    else:
        print(num)

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("Hay ",contador," números pares entre ellos")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - ")