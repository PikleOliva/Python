print("-------------------------------------------------------") 
print("Matriz3: AUTOMOTRIZ") 
print("-------------------------------------------------------") 
#Inicializar 
Mat = [] 
# #Entradas 

anios = int( input("Ingresar cuántos años se desean analizar: ")) 
sucur = int( input("Ingresar cuántos sucursales se desan analizar: ")) 
# Inicializamos variables
max=0
ventas=0
ventastot=0
maxanual=0
anual=0
# Ingresar datos a la matriz
for i in range(anios):
        Mat.append( [] ) 
        #Se agrega la fila i 
        for j in range(sucur): 
            elemento = input( "Ventas del año {} de la sucursal {}: ".format(i+1, j+1) )
            Mat[i].append( int(elemento)) 
print (Mat) # Para ver cómo quedó la carga de datos

# Cálculo de las ventas anuales
for i in range(anios):
    for j in range(sucur):
        ventas=ventas + (Mat[i][j])
    
# Selección del año con mayor número de ventas
        if ventas>maxanual:
            maxanual=ventas
            anual=i+1
    print("El año de mayor venta fue el ",anual," con ventas por ",ventas)
    print ("El año ",i+1," las ventas fueron de  ",ventas)
ventas=0

# Vuelvo a cero ventas para empezar otro proceso
ventas=0  
# Ahora veo las ventas de cada sucursal por cada año
for i in range(sucur):
    for j in range(anios):
        ventas=ventas + (Mat[j][i])
        ventastot=ventastot+ventas
        print ("La sucursal ",i+1," vendió ",ventas," en el año ",j+1)
# Calculo la sucursal con mayor número de ventas y el año en que se produjo
        if ventas>max:
             max=ventas
             sucur=i+1
             aniete=j+1
        ventas=0
print("La sucursal que más vendió fue la ",sucur," que vendió ",max," en el año ",aniete)
print("----------")        
print("Las ventas totales fueron de ",ventastot)
print("----------")        
print("El promedio de ventas por año fue de ",ventastot/anios)
print("----------")    
