from math import * 
print("-------------------------------------------------------------")
print("DETERMINAR CUÁNTAS VECES APARECE EL CARACTER 'a'")
print("-------------------------------------------------------------")

cant=int(input("¿Cuántas letras queres comparar?: "))
cont=0
for i in range(cant):
    car=input("Ingresar una letra: ")
    if car=='a':
        cont=cont+1
print("-------------------------------------------------------------")
print("En la serie de ",cant," letras hay ",cont," letras 'a'")
print("-------------------------------------------------------------")

