import math

print ("-------------------------------------------------")
print ("Ejercicio - Tiempo de encuentro de dos móviles")
print ("-------------------------------------------------")
#Ingresamos los velocidades y la distancia

Va = float (input ("Ingresar velocidad del primer móvil (km/h):" ))
Vb = float (input ("Ingresar velocidad del segundo móvil (km/h):" ))
distancia = float (input ("Ingresar La distancia que separa los dos puntos b(en km):" ))

#cálculos
Vams = Va*5/18
Vbms=Vb*5/18
te = float(distancia*1000/(Vams+Vbms))
min=te/60
hora=min/60
#Ahora imprimimos los resultados
print ("-------------------------------------------------")
print ("El tiempo de encuentro entre los móviles es de: ",te," segundos (",min," minutos o ",hora," horas)")
print ("-------------------------------------------------")
