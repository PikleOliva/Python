print("-------------------------------------------------------------")
print("CALCULAR LA SUMA DE LOS DIVISORES DE UN NÚMERO")
print("-------------------------------------------------------------")

# Ingresamos un número. Para salir del programa introducir un número negativo




num=int(input("Ingreaar un número. (Nro. negativo para salir)"))

while num!=0:

    suma=0
    for i in range(1,num+1):
        if num % i == 0:
            suma = suma + i



    print("-------------------------------------------------------------")
    print("La suma de lo divisores de ",num," es ",suma)
    print("-------------------------------------------------------------")

    num=int(input("Ingraar un número. (Nro. negativo para salir)"))
