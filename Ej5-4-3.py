print("-------------------------------------------------------------")
print("CALCULAR LOS NUMEROS PRIMOS DE 1 A 1000")
print("-------------------------------------------------------------")

# Los primos son divisibles únicamente por uno y por sí mismos.
# tengo que definir dos variables, i y j, de manera tal de poder ir dividiendo i por j.
# Empezamos diciendo que primo es true. Luego entramos en un ciclo for while que va desde i=2 (el primer primo)
# hasta 1000. Y while j<i vamos probando la división entre i/j. Si en algún momento el módulo de la división
# resula ser cero, transformamos primo en false y le metemos un break. Con eso salimos del for y vuelve el while
# a tomar el dominio, estableciendo primo true .

print ("Ingresar entre qué números querés saber cuántos y cuáles son los número primos: ")

inicio=int(input("Desde qué número queres empezar? "))
fin=int(input("¿Hasta qué número? "))

contador=0

for i in range(inicio,fin):

    j=2
    primo=True

    while j<i and primo==True:
        if i%j==0:
            primo=False
            break
        else:
            j=j+1

    if primo==True:
        print (i,"es primo")
        contador=contador+1
        
print("-------------------------------------------------------------")
print("Entre 1 y ",fin," hay ",contador," números primos")
print("-------------------------------------------------------------")
