print("----------------------------------------------------")
print("ORDENAR Y QUITAR LOS ELEMENTOS DE UN VECTOR")
print("----------------------------------------------------")

# Inicializamos las variables un vector vacío

Vector=[]

tot=int(input("Ingresar el número de elementos a introducir: "))

for i in range(1,tot+1):
    registro=input("Ingresar el primer registro {0}: ".format(i))
    Vector.append(registro)

print(Vector)