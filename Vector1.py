print("----------------------------------------------------")
print("LLENAR Y LEER UN VECTOR")
print("----------------------------------------------------")

# Inicializamos un vector vacío

cant=int(input("¿Cuántos elementos tendrá el vactor?: "))
i=1
Vector=[]

# Ahora lo llenamos

for i in range(cant):
    
    valor=int(input("Ingresamos: "))
    Vector.append(valor)

# Ahora vemos qué tiene adentro

print("----------------------------------------------------")
print(Vector)
print("----------------------------------------------------")
