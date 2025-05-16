import math
print("-------------------------------------------------------------")
print("TRIÁNGULO O CÍRCULO")
print("-------------------------------------------------------------")

#print("Seleccionar la opción")
print("1 - Triángulo")
print("2 - Círculo")

opcion = int(input("Ingresar la opción elegida: "))

if opcion == 1:
    lado=int(input("Ingresar el valor del lado del triángulo: "))
    
    print("-------------------------------------------------------------")
    print("La superficie del triángulo es ",(3**0.5)*(lado**2)/4)
    print("-------------------------------------------------------------")

elif opcion==2:
    radio=int(input("Ingresar el valor delradio del círculo: "))
    
    print("-------------------------------------------------------------")
    print("La superficie del círculo es ",math.pi*radio**2)
    print("-------------------------------------------------------------")

 
    
else:
    print("-------------------------------------------------------------")
    print("Opción incorrecta")
    print("-------------------------------------------------------------")