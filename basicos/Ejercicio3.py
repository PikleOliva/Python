print ("-------------------------------------------------")
print ("Ejercicio 3- PUNTAJE DE EXAMEN")
print ("-------------------------------------------------")
#Ingresaremos la cantidad de respuestas correctas, incorrectas y sin responder
RC = int (input ("Ingresar el numero de respuestas correctas (3 pts. cada una): "))
RI = int (input ("Ingresar el numero de respuestas incorrectas (-1 pts. cada una): "))
SR = int (input ("Ingresar el numero de preguntas sin responder (No agrega puntos): "))
#Ahora calculamos el puntaje que obtuvo el alumno
PE = float(RC*3+RI*(-1)+SR*0)
print ("-------------------------------------------------")
print ("El puntaje de examen obtenido es: ",PE)
print ("-------------------------------------------------")

