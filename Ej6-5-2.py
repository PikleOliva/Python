print("-------------------------------------------------------")
print("Complemento2: INVERTIR VECTOR DE CARACTERES.") 
print("-------------------------------------------------------") #Entradas 
print("Ingrese dimensión del vector: ")
n = int( input()) 
v = n*[''] 
#Se inicializa un vector con valores por defecto 
for i in range(n): 
    v[i] = input("Ingrese Caracter: ") 
#Proceso 
z = '' 
d = n 
for i in range(n//2): 
    z = v[i] 
    v[i] = v[d-1] 
    v[d-1] = z 
    d = d - 1 
    #Salida 
for i in range(n): 
        print(v[i])