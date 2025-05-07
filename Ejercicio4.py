print ("-------------------------------------------------")
print ("Ejercicio 4- PUNTAJE DE PARTIDOS")
print ("-------------------------------------------------")
#Ingresaremos la cantidad de respuestas correctas, incorrectas y sin responder
RC = int (input ("Ingresar el numero de partidos ganados (3 pts. cada uno): "))
RI = int (input ("Ingresar el numero de partidos empatados (1 pts. cada uno): "))
SR = int (input ("Ingresar el numero de partidos perdidos (No agrega puntos): "))
#Ahora calculamos el puntaje que obtuvo el alumno
PE = float(RC*3+RI)
print ("-------------------------------------------------")
print ("El puntaje obtenido por el Club es: ",PE)
print ("-------------------------------------------------")
