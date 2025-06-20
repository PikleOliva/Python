import math

def rayas(n):
    for i in range(n):
        print("-",end=" ")
    print("")

def suma(a, b):
    suma=a+b
    return suma
def resta(a,b):
    resta=a-b
    return resta
def multip(a,b):
    multiplicacion=a*b
    return multiplicacion
def division(a,b):
    division=a/b
    return division
def potencia (a,b):
    potencia=a**b
    return potencia

rayas(20)
a=int(input("Ingresar el primer numero: "))
b=int(input("Ingresar el segundo numero: "))
rayas(20)
print()
rayas(20)
resultado=suma(a,b)
print("La suma de ",a," y ",b," da ",resultado)
rayas(20)
print()
rayas(20)
resultado=resta(a,b)
print("La resta de ",a," menos ",b," da ",resultado)
rayas(20)
print()
rayas(20)
resultado=multip(a,b)
print("El producto de ",a," por ",b," da ",resultado)
rayas(20)
print()
rayas(20)
resultado=round(division(a,b),4)
print(a," dividido ",b," da ",resultado)
rayas(20)
print()
print()
rayas(20)
resultado=potencia(a,b)
print(a," elevado a la  ",b," da ",resultado)
rayas(20)



