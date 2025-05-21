print("----------------------------------------------------")
print("DETERMINAR LA TEMPERATURA MEDIA Y LAS QUE LA SUPERAN")
print("----------------------------------------------------")

# Inicializamos las variables un vector vacío

media= 0.000
suma=0
cant=int(input("¿Cuántos elementos tendrá el vactor?: "))
#i=1
Tempe=[]
cont=0
mayor=0
# Ahora lo llenamos

for i in range(cant):
    
    valor=float(input("Temperatura: "))
    Tempe.append(valor)
    suma=suma+valor
    cont=cont+1
media=suma/cont
for i in range(cant):
    if Tempe[i]>media:
        mayor=mayor+1



# Ahora vemos qué tiene adentro

print("----------------------------------------------------")
print("La temperatura media fue ",media)
print("Hubo ",mayor," temperaturas superiores a la media")
print("----------------------------------------------------")
