print("-------------------------------------------------------") 
print("Matriz3: AUTOMOTRIZ") 
print("-------------------------------------------------------") 
#Inicializar 
Mat = [] 
# #Entradas 

anios = int( input("Ingresar cuántos años se desean analizar: ")) 
sucur = int( input("Ingresar cuántos sucursales se desan analizar: ")) 
#Proceso 
max=0
ventas=0
ventastot=0
    #Ingresar datos al array 
for i in range(anios):
        Mat.append( [] ) 
        #Se agrega la fila i 
        for j in range(sucur): 
            elemento = input( "Ventas del año {} de la sucursal {}: ".format(i+1, j+1) )
            Mat[i].append( int(elemento)) 
print (Mat)
for i in range(sucur):
    for j in range(anios):
        ventas= ventas + Mat[i][j]
        ventastot=ventastot+ventas
        print ("La sucursal ",i+1," vendió ",ventas," en el año ",j+1)
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
