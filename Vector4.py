import random, math

print("----------------------------------------------------")
print("SUMAR DOS VECTORES")
print("----------------------------------------------------")

# Creamos tres vectores vacíos

Vect_1=[]
Vect_2=[]
Vect_Suma=[]

# Seleccionamos cuántos registros van a tener los vectores (tienen que ser iguales)
reg=int(input("Ingresar el número de elementos a introducir: "))

# Llenamos el vector de origen
for i in range(reg):
    reg_1=input("Ingresar el registro: {0} ".format(i))
    Vect_1.append(reg_1)
print(Vect_1)
for i in range(reg):
    reg_1=input("Ingresar el registro: {0} ".format(i))
    Vect_2.append(reg_1)
print(Vect_2)
for i in range(reg):
    Vect_Suma==(Vect_1+Vect_2)
# Lo mostramos para ver lo que incorporamos, si hay repetidos y si está sin ordenar
print(Vect_Suma)

