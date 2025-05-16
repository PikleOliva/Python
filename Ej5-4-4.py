print("-------------------------------------------------------------")
print("ESCRIBIR LOS ´DÍGITOS QUE INTEGRAN UN NÚMERO ")
print("-------------------------------------------------------------")

# El fundaento es que a medida que vamos dividiendo por diez, el resto que nos queda el es dígito de la unidad,
# luego de la decena, etc.

num=int(input("Ingresar el número que se quiere descomponer en dígitos "))

while num>0:
    resto=num%10
    print (resto)
    num=num//10
    



print("-------------------------------------------------------------")
print("")
print("-------------------------------------------------------------")
