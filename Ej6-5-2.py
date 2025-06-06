print("-------------------------------------------------------")
print("Complemento2: INVERTIR VECTOR DE CARACTERES.") 
print("-------------------------------------------------------") #Entradas 

num = int(input("Longitud de la palabra: ")) 
Vector = num*[''] 
#Se inicializa un vector con valores por defecto 
for i in range(num): 
    Vector[i] = input("Ingrese Caracter: ") 
#Proceso 
z = '' 
d = num 
for i in range(num//2): 
    z = Vector[i] 
    Vector[i] = Vector[d-1] 
    Vector[d-1] = z 
    d = d - 1 
    #Salida 
for i in range(num): 
    print(Vector[i],end="  ,  ")
