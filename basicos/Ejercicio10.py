print ("-------------------------------------------------")
print ("Ejercicio 10 - ÁREA Y VOLUMEN DEL CILINDRO")
print ("-------------------------------------------------")
#Ingresamos dos variables (radio y altura) Pi es constante
radio = int (input("Ingresar el radio del cilindro (cm): "))
altura = int (input ("Ingresar la altura del cilindro (cm): "))
Pi = float (3.14)
#Calculamos area y volumen
area= float((2*Pi*radio*radio)+(2*Pi*radio*altura))
volumen = float (Pi*radio*radio*altura)
#Ahora imprimimos los resultados
print ("-------------------------------------------------")
print ("La superficie del cilindro es de: ",area)
print ("-------------------------------------------------")
print ("El volumen del cilindro es de: ",volumen)
print ("-------------------------------------------------")