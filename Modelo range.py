print("-------------------------------------------------------------")
print("ESTE ES EL MODELO DE CÓMO SE USA 'range' EN PYTHON")
print("-------------------------------------------------------------")

# Python no tiene el for como java. Trabaja sobre una lista. La lista se crea 
# con 'range'. El 'for' itera todos los elementos de la lista. Las listas van 
# entre corchetes '[]'. Los elementos se separan con comas ',' 
# Range lleva parámetros Si tiene un solo parámetro la cuenta comienza en cero. 
# OJO, la primera casilla es la número 0. Si tiene dos parámetros, indica principio 
# y fin. Si tiene tres, indica principio, fin y el 'paso' de la secuencia

lista = range(3)

for valor in lista:
    print (valor)
print("")
# Al ejecutarlo aparece esto 

# -------------------------------------------------------------
# ESTE ES EL MODELO DE CÓMO SE USA 'range' EN PYTHON
# -------------------------------------------------------------
# 0
# 1
# 2

lista = range(5, 8)

for valor in lista:
    print (valor)
print("")

# Al ejecutarlo aparece esto

# -------------------------------------------------------------
# ESTE ES EL MODELO DE CÓMO SE USA 'range' EN PYTHON
# -------------------------------------------------------------
# 5
# 6
# 7

lista = range(5, 18, 4)

for valor in lista:
    print (valor)
print("")

# Al ejecutarlo esto es lo que aparece

# -------------------------------------------------------------
# ESTE ES EL MODELO DE CÓMO SE USA 'range' EN PYTHON
# -------------------------------------------------------------
# 5
# 9
# 13
# 17