from random import * 
print("-------------------------------------------------------------")
print("MOSTRAR LOS PRIMEROS DIEZ NÚMEROS PRIMOS Y SUS CUBOS (EMPEZANDO CON 2)")
print("-------------------------------------------------------------")

inicio=int(2)
fin=int(31)

contador=0

for i in range(inicio,fin):

    j=2
    primo=True

    while j<i and primo==True:
        if i%j==0:
            primo=False
            break
        else:
            j=j+1

    if primo==True:
        cubo=i**3
        print (i,"es primo y su cubo es ",cubo)
        contador=contador+1
        
print("-------------------------------------------------------------")
print("")
print("-------------------------------------------------------------")
