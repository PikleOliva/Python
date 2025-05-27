print("-------------------------------------------------------") 
print("Matriz2: VERIFICAR SI LA MATRIZ ES SIMÉTRICA.") 
print("-------------------------------------------------------") 
#Inicializar 
Mat = [] 
# #Entradas 

filas = int( input("Ingrese dimensiones del arreglo: ")) 
#Proceso 

    #Ingresar datos al array 
for i in range(filas):
        Mat.append( [] ) 
        #Se agrega la fila i 
        for j in range(filas): 
            elemento = input( "Ingresar el elemento {}{} de la matriz: ".format(i+1, j+1) )
            Mat[i].append( int(elemento)) 
sim = True 
i = 0 
while i < filas and sim == True: 
        j = 0 
        while j < i-1 and sim == True:
            if Mat[i][j] == Mat[j][i]: 
                j = j + 1 
            else: 
                sim = False
        i = i + 1 
if sim: print("La matriz es simétrica") 
else: print("La matriz NO es simétrica") 
