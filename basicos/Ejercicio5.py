print ("-------------------------------------------------")
print ("Ejercicio 5- NUMERO DE MICRODISCOS NECESARIOS")
print ("-------------------------------------------------")
#Ingresaremos la capacidad del disco rígido en MBy
CD = int (input ("Ingresar la capacidad del disco rígido (en GBy): "))
#Ahora calculamos la cantidad de disquettes de 1.44 MBy necesarios
DB = float(CD*1024/1.44)
print ("-------------------------------------------------")
print ("Se necesitarán ",DB, " de 1.44 MBy para respaldo del disco rígido")
print ("-------------------------------------------------")

