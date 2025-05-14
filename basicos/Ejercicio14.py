import math

print ("-------------------------------------------------")
print ("Ejercicio - Lado desconocido del triángulo (teo del coseno)")
print ("-------------------------------------------------")
#Ingresamos los dos lados y el ángulo comprendido

ladoa = float (input ("Ingresar el primer lado:" ))
ladob = float (input ("Ingresar el segundo lado:" ))
angulo = float (input ("Ingresar el valor del ángulo comprendido:" ))

#cálculos
ladoc=int((ladoa**2+ladob**2-2*ladoa*ladob*math.cos(angulo*math.pi/180) )**0.5)

#Ahora imprimimos los resultados
print ("-------------------------------------------------")
print ("El tercer lado del triángulo mide: ",ladoc)
print ("-------------------------------------------------")
