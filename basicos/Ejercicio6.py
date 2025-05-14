print ("-------------------------------------------------")
print ("Ejercicio 6 - DISTANCIA ENTRE DOS PUNTOS EN EL PLANO")
print ("-------------------------------------------------")
#Ingresaremos las coordenadas x e y de los dos puntos
x1 = int (input ("Ingresar el valor de la coordenada x del punto 1: "))
y1 = int (input ("Ingresar el valor de la coordenada y del punto 1: "))
x2 = int (input ("Ingresar el valor de la coordenada x del punto 2: "))
y2 = int (input ("Ingresar el valor de la coordenada y del punto 2: "))

#Ahora calculamos la distrancia entre los puntos

distancia = float((((x2-x1)**2+(y2-y1)**2))**0.5)
print ("-------------------------------------------------")
print ("La distancia entre los puntos 1 y 2 es de: ",distancia)
print ("-------------------------------------------------")

