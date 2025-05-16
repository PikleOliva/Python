from random import * 
print("-------------------------------------------------------------")
print("MOSTRAR LOS PRIMEROS DIEZ NÚMEROS PARES Y SUS CUBOS (EMPEZANDO CON 2)")
print("-------------------------------------------------------------")

contador= int (0)
inicio = int(2)
fin = int(21)
num = int(2)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - ")
for i in range(inicio,fin+1,2):
    
    if num%2==0:
        cubo=num**3
        print(num," - ",cubo)
        num=num+2
    
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("CALCULADORA DE CUBOS")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - ")


base=int(input("Engresar el número del cual se desea conocere el cubo: "))
cubito= base**3
print("")
print("El cubo de ",base," es ",cubito)
