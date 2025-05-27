print("-------------------------------------------------------") 
print("COMPLETAR Y SUMAR 2 MATRICES") 
print("-------------------------------------------------------") 
#Inicializar 
Mat1 = [] 
Mat2 = [] 
MatSuma = [] 
# #Entradas 
print ("Ingrese dimensión de la matriz,máximo 100") 
filas = int( input("Número de Filas: ")) 
col = int( input("Número Columnas: ")) 
#Proceso 

print("-------------------------------------------------------") 
print("Datos Matriz 1") 
print("-------------------------------------------------------") 


for i in range(filas): 
    Mat1.append( [] ) 
    #Agregamos una i fila vacía en A 
    for j in range(col): 
        Mat1[i].append( int( input("Elemento {}{} de la matriz 1: ".format(i+1,j+1)))) 

print("-------------------------------------------------------") 
print("Datos Matriz 2") 


for i in range(filas):
    Mat2.append( [] )
    #Agregamos una i fila vacía en B 
    for j in range(col): 
        Mat2[i].append( int( input("Elemento {}{} de la matriz 2: ".format(i+1,j+1)))) 
for i in range(filas):
    MatSuma.append( [] ) 
    #Agregamos una i fila vacía en C ç
    for j in range(col): 
        MatSuma[i].append( Mat1[i][j] + Mat2[i][j]) 
        #Salida 
print("\nSALIDA: ") 
print("-------------------------------------------------------") 
print("Matria 1: ",Mat1) 
print("Matria 2: ",Mat2) 
print("Matria Suma: ",MatSuma)