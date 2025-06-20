import math

def rayas(n):
    for i in range(n):
        print("-",end=" ")
    print("")
def esPar(numero):
    if numero%2==0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

rayas(40)
print("Determinar si un número es par o impar")
rayas(40)
numero=int(input("Ingresar el número a estudiar: "))
resul=esPar(numero)

def maximo(nu1, num2, num3):
    max=max(num1, num2, num3)
    return max

num1=int(input("Ingresar un número: "))
num2=int(input("Ingresar un número: "))
num3=int(input("Ingresar un número: "))
maxi=max(num1, num2, num3)
print(f"El máximo entre {num1}, {num2} y {num3} es {maxi}")
rayas(20)
print("FACTORIAL DE UN NUMERO")
rayas(20)

def factorial(numero):
    numero=int(input("Ingresar un número: "))
    if numero==0:
        factorial=1
        return factorial
    else:
        i=1
        factorial=1
        for i in range(1, i+1):
            factorial=factorial*i
        return factorial


verde=factorial(numero)
print(verde)