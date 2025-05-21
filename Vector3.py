import random, math
print("----------------------------------------------------")
print("ORDENAR Y QUITAR LOS ELEMENTOS DE UN VECTOR")
print("----------------------------------------------------")

# Creamos dos vectores vacíos

Vector=[]
VectorNuevo=[]

# Seleccionamos cuántos registros vamos a ingresar
tot=int(input("Ingresar el número de elementos a introducir: "))

# Llenamos el vector de origen
for i in range(1,tot+1):
    registro=input("Ingresar el registro: {0}".format(i))
    Vector.append(math.trunc(random.random()*100))

# Lo mostramos para ver lo que incorporamos, si hay repetidos y si está sin ordenar
print(Vector)

# Ahora le pedimos que se fije, para cada registro que incorporamos, si ya está en el vector nuevo.
# Si no está, que lo agregue. 

for registro in Vector:
    if registro not in VectorNuevo:
        VectorNuevo.append(registro)

# Ahora que nos muestre el vector reducido, pero sin ordenar
print (VectorNuevo)

# Por último, que ordene el vector nuevo
VectorNuevo.sort()


print (VectorNuevo)
