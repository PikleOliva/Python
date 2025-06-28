import random
def dibujarRayas():
    for i in range(40):
        print("-", end=(" "))
    print()

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

a= int(input("Ingresar primer número: "))
b= int(input("Ingresar el otro número: "))
resultado=float
dibujarRayas
resultado=sumar(a,b)
print (resultado)
dibujarRayas
resultado=restar(a,b)
print (resultado)
dibujarRayas
resultado=multipli(a,b)
print (resultado)
dibujarRayas
resultado=round(divide(a,b),4)
print (resultado)
dibujarRayas
resultado=potencia(a,b)
print (resultado)
dibujarRayas
resultado=round(raiz(a,b),4)
print (resultado)
dibujarRayas
print()
for i in range(1,6):
    resultado=sumar(i,i+1)
    print (resultado)
print()
for i in range(1,6):
    resultado=multipli(7,i)
    print(resultado)

arreglo=[]
for i in range (4):
    arreglo.append(int(input("Ingresar un número: ")))
   
print(arreglo)
for i in range(4):
    print(f"El número de índice {i} es {arreglo[i]}")

arreglo=[]
for i in range(4):
    arreglo.append(input("Ingresar una palabra: "))
print (arreglo)
arreglo=[]

for i in range (3):
    arreglo.append([])
    for j in range(2):
        arreglo[i].append(int(input(f"Ingresar el registro {i},{j}: ")))
    
print (arreglo)
for i in range(3):
    print(arreglo[i])

arreglo=[]
largo=int(input("Ingresar la longitud del arreglo: "))
for i in range(largo):
    arreglo.append(input(f"Ingresar el nombre de la posición {i+1}: "))
    
for i in range(largo):
    print (arreglo[i]) 
print (arreglo)

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
filas=int(input("Número de filas: "))
columnas=int(input("Número de columnas: "))
Matriz=cargaMatriz2(filas,columnas)
dibujarRayas()
for i in range(filas):
    print(Matriz[i])
dibujarRayas()

registros=int(input("Ingresar el número de registros: "))
dibujarRayas()
print("Carga de datos del primer vector")
dibujarRayas()
Vector1=cargaVector(registros)
dibujarRayas()
print("Carga de datos del segundo vector")
dibujarRayas()
Vector2=cargaVector(registros)
VectorSuma=[]

for i in range(registros):
   suma=Vector1[i]+Vector2[i]
   VectorSuma.append(suma)
dibujarRayas()
print(VectorSuma)
dibujarRayas()

for i in range (10):
    num=round(random.random()*100)
    pot=potencia(num,2)
    square=round(raiz(num,2),4)
    print(f"El cuadrado de {num} es {pot} y la raíz cuadrada es {square}")