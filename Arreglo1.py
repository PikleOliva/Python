
def dibujarRayas():
    for i in range(40):
        print("-", end=(" "))
    print()
def cargaVector(registros):
    Vector=[]
    for i in range(registros):
        Vector.append(int((input("Ingresar el registro: "))))
    return Vector
def sumar(a, b):
    resultado=a+b
    return resultado
suma=[]
arreglo=[]
invertido=[]
largo=int(input("Indicar la longitud del arreglo: "))
arreglo=cargaVector(largo)
print("El arreglo original era ",arreglo)
for i in range(largo):
    
    invertido.append(arreglo[largo-1-i])
    #print (invertido)
print ("El arreglo invertido es ",invertido)

dibujarRayas()
print("AHORA VAMOS A SUMAR LOS DOS ARREGLOS")
dibujarRayas()

for i in range(largo):
    termino=sumar(arreglo[i],invertido[i])
    suma.append(termino)
print(suma)

posi=0
nega=0
cero=0
largo=int(input("Ingresar el largo del vector "))
arreglo=[]
arreglo=cargaVector(largo)
print (arreglo)
for i in range(largo):
    if arreglo[i]>0:
        posi=posi+1
    elif arreglo[i]<0:
        nega=nega+1
    else:
        cero=cero+1
print(f"El arreglo tiene {posi} elementos positivos, {nega} negativos y {cero} ceros")