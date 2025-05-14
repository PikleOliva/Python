print("------------------------------------------------------")
print("ORDENAR DOS NUMEROS INGRESADOS")
print("------------------------------------------------------")

#PRIMERO VAMOS A INGRESAR LOS NÚMEROS

primo = int (input ("Ingresar un número: "))
secondo = int (input ("Ingresar otro número: "))

if primo<secondo:
    print ("De menor a mayor el orden es ",primo, " ",secondo)
else:
    print ("De menor a mayor el orden es ",secondo," ", primo)
