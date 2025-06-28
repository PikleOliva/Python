# Funciones: 
# dibujar Rayas
# cargar Vector
# cargar Matriz
# sumar
# restar
# multiplicar
# dividir
# potencia
# raiz

def dibujarRayas():
    for i in range(40):
        print("-", end=(" "))
    print()
def cargaVector(registros):
    Vector=[]
    for i in range(registros):
        Vector.append(int((input("Ingresar el registro: "))))
    return Vector

def cargaMatriz2(filas,columnas):
    Matriz=[]
    for i in range(filas):
        Matriz.append([])
        for j in range(columnas):
            Matriz[i].append(int(input(f"Ingresar el registro fila {i+1}, columna {j+1}: ")))
    return Matriz
def sumar(a, b):
    resultado=a+b
    return resultado
def restar(a, b):
    resultado=a-b
    return resultado
def multipli(a, b):
    resultado=a*b
    return resultado
def divide(a, b):
    resultado=a/b
    return resultado
def potencia(a,b):
    resultado=a**b
    return resultado
def raiz(a,b):
    resultado=a**(1/b)
    return resultado
