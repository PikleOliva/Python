print("----------------------------------------------------")
print("SUMAR DOS MATRICES (DEBEN TENER IGUAL NÚMERO DE FILAS Y COLUMNAS)")
print("----------------------------------------------------")

# 

Mat1=[]
Mat2=[]


# Establecemos la dimensión de la matriaz. 
fila=int(input("Ingresar el número de filas de las matrices: "))
col=int(input("Ingresar el número de columnas de las matrices: "))

print("Ingresar los elemetos de la matriz 1")
for i in range(fila):
    Mat1.append([])
    for j in range(col):
        Mat1[i].append(int(input("ingresar e valor del elemento: "))   )
print (Mat1)
print("------------")
print("Ingresar los elemetos de la matriz 2")
for i in range(fila):
    Mat2.append([])
    for j in range(col):
        Mat2[i].append(int(input("ingresar e valor del elemento: ")))   
print (Mat2)

print("--------------")
Mat3=[]

for i in range(fila):
    for j in range(col):
        Mat3.append(Mat1+Mat2)
print (Mat3)
