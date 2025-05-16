print("-------------------------------------------------------------")
print("ESTE ES EL MODELO DE CÓMO SE USA 'for y range' EN PYTHON")
print("-------------------------------------------------------------")

# Python no tiene el for como java. Trabaja sobre una lista. La lista se crea 
# con 'range'. El 'for' itera todos los elementos de la lista. Las listas van 
# entre corchetes '[]'. Los elementos se separan con comas ','

lista = [1,45,12,3]

for valor in lista:
    print (valor)
print("")

# La lista se puede formar automáticamente con 'rango'. 'rango' acepta parámetros de inicio, fin y paso
# Por ej, rango(10) crea una lista del 0 al 9; rango(3,8) cre una lista que va de 3 a 7; rango(2,8,2) 
# crea una lista que empieza en 2, sigue en 4 y termina en 6 (porque llegaría solo a 7)

lista= range(5)

for i in lista:
    print (i)
print("")
for i in lista:
    if i==3:
        continue
    print (i)
print("")
for i in lista:
    if i==3:
        break
    print(i)
