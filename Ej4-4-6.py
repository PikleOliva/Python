print("-------------------------------------------------------------")
print("EL NÚMERO DEFINE")
print("-------------------------------------------------------------")

uno=int(input("Ingresar el primer número: "))
dos=int(input("Ingresar el segundo número: "))
tres=int(input("Ingresar el tercer número: "))

if uno<0:
    res=dos*tres

    print("-------------------------------------------------------------")
    print("El primer número fue negativo. El producto de los dos restantes es: ",res)
    print("-------------------------------------------------------------")
else:
    res=uno+dos+tres
    print("-------------------------------------------------------------")
    print("El primer número fue positivo. La suma de los tres es: ",res)
    print("-------------------------------------------------------------")
