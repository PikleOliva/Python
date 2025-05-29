print("-------------------------------------------------------") 
print("Matriz 6-5-1: PRODUCTO ESCALAR Y VECTORIAL DE DOS VECTORES") 
print("-------------------------------------------------------") 
#Inicializar 
Vector1 = [] 
Vector2 = []

# #Entradas 

elem = int( input("Ingresar cuántos elementos tienen los vectores: ")) 

# Inicializamos variables
escalar=0
# Ingresar datos a los vectores
for i in range(elem):
        Vector1.append(int(input("Elemento Nº {} del Vector 1: ".format(i+1)))) 
        
for i in range(elem):
        Vector2.append(int(input("Elemento Nº {} del Vector 2: ".format(i+1)))) 

print (Vector1)
print (Vector2)
# Para ver cómo quedó la carga de datos

# Cálculo del producto escalar
for i in range(elem):
    prodescal=Vector1[i]*Vector2[i]
    escalar=escalar+prodescal
print("El producto escalar es ",escalar)

# Cálculo de producto vectorial
x=Vector1[1]*Vector2[2]-Vector1[2]*Vector2[1]
y=-Vector1[0]*Vector2[2]+Vector1[2]*Vector2[0]
z=Vector1[0]*Vector2[1]-Vector1[1]*Vector2[0]

print("El producto vectorial es: {} i , {} j , {} k".format (x,y,z))