print ("-------------------------------------------------")
print ("Ejercicio 13 - CAMBIO DEL ARBOLITO")
print ("-------------------------------------------------")
#Ingresamos la cantidad de pesos
pesos = float (input("Ingresar la cantidad de pesos que quiere cambiar: "))
dolar=1080
euro=1239.70

#Ahora imprimimos los resultados
print ("-------------------------------------------------")
print ("Usted podrá comprar " ,"{:.4f}".format(pesos/dolar), " dólares estadounidenses")
print ("-------------------------------------------------")
print ("Usted podrá comprar " ,"{:.4f}".format(pesos/euro), " euros")
print ("-------------------------------------------------")
