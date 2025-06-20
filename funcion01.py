import math
def supTriangulo(base, altura):
    area=base*altura/2
    return area

def rayas(n):
    for i in range(n):
        print("-",end=" ")
    print("")

def circulo(radio):
    area=math.pi*radio**2
    return area

def nombrePorTeclado(nombre):
    return nombre

rayas(20)
base=int(input("Ingresar el valor de la base: "))
altura=int(input("Ingresar el valor de la altura: "))
resultado=supTriangulo(base, altura)
print("La superficie del triángulo es: ",resultado)
rayas(20)

rayas (20)
radio=int(input("Ingresar el valor del radio del círculo: "))
resultado=round(circulo(radio),2)
print("la superficie del círculo es: ",resultado)
rayas(20)

rayas(20)
nom=input("Ingresar el nombre: ")
nombre=nombrePorTeclado(nom)
ape=input("Ingresar el apellido: ")
apellido= nombrePorTeclado(ape)
print("Tu nombre completo es ",nombre, apellido)
rayas(20)

