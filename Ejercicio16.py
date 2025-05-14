import math

print ("-------------------------------------------------")
print ("Ejercicio - Conversión de ángulos")
print ("-------------------------------------------------")
#Ingresamos los el ángulo que queremos convertir

rad = float (input ("Ingresar el valor del ángulo (rad):" ))

#cálculos
sexa= rad*180/math.pi
cent=rad*200/math.pi

#Ahora imprimimos los resultados
print ("-------------------------------------------------")
print ("El ángulo de ",rad," radianes mide ","{:.2f}".format(sexa)," º o ","{:.2f}".format(cent)," grandos centesimales")
print ("-------------------------------------------------")
