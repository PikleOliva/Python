import math
import random

print("-------------------------------------------------------")
print("Complemento3: INTERACTUAR CON UN VECTOR A TRAVÉS DE OPCIONES")
print("-------------------------------------------------------")
print("")
#inicializar
tamanio=int(input("Ingresar el tamaño del vector (máx 100): "))
i=0
Vector=[""]*tamanio
opcion=-1
print("-----------------------------------")
print("          M E N Ú    ")
print("-----------------------------------")
print("")
print("1 - Llenar un vector con elementos nulos")
print("2 - Llenar un vector con elementos aleatorios")
print("3 - Llenar un vector con elementos secuenciales (con inicio en 'a' y paso 'b')")
print("4 - Llenar un vector con elementos selecionados")
print("5 - Dado un vector, reemplazar uno de sus registros (por posición)")
print("6 - Dado un vector, reemplazar uno de sus registros (por valor)")
print("7 - Dado un vector, eliminar uno de sus registros (por posición)")
print("8 - Dado un vector, eliminar uno de sus registros (por valor)")
print("")
print("-----------------------------------")

while opcion!=0:
    opcion=int(input("Ingresar la opción elegida (0 para salir): "))
    if opcion ==1:
        print("Llenar un vector con elementos nulos")
        Vector = tamanio * [0]
        print (Vector)

    elif opcion ==2:
        i=0
        print("Llenar el vector con elementos aleatorios")
        for i in range(tamanio): 
            Vector[i]= int(math.trunc(random.random()*100))
        print (Vector)

    elif opcion==3:
        print("Llenar el vector con elementos secuenciales (empezando con a)")
        a=int(input("¿Con qué número querés empezar?: "))
        b=int(input("¿Qué paso querés que tenga el vector?: "))
        for i in range(tamanio):
            Vector[i]=int(a)
            a=a+b
        print(Vector)

    elif opcion==4:
        print("Llenar el vector con elementos seleccionados)")
        for i in range(tamanio):
            Vector[i]=int(input("ingresar el elemento: "))
        print (Vector)

    elif opcion == 5:
        i=0
        for i in range(tamanio): 
            Vector[i]= int(math.trunc(random.random()*100))
        print (Vector)
        i=int(input("¿Qué registro del vector desea reemplazar?: "))-1
        if i<tamanio:
            elemento=int(input("Qué valor desea asignarle al elemento: "))
            Vector[i]=elemento
            print (Vector)
    elif opcion == 6:
        i=0
        print("Llenar el vector con elementos aleatorios)")
        for i in range(tamanio): 
            Vector[i]= int(math.trunc(random.random()*100))
        print (Vector)
        valor=int(input("¿Qué valor del vector desea reemplazar?: "))
        if valor in Vector:
            i=Vector.index(valor)
            if i<tamanio:
                elemento=int(input("Qué valor desea asignarle al elemento: "))
                Vector[i]=elemento
            print (Vector)

    elif opcion==7:
        Copia=(tamanio-1)*['']
        print("Llenar el vector con elementos aleatorios)")
        for i in range(tamanio):
            Vector[i]= int(math.trunc(random.random()*100))
        print ("El vector ingresado es ",Vector)
        reg=int(input("¿Qué registro del vector desea eliminar?: "))-1
    
        i=0
        while i<reg:
            for i in range(tamanio-1):
                Copia[i]=Vector[i]
                i+1
        for i in range(reg,tamanio-1):
            Copia[i]=Vector[i+1]
        Vector=Copia
        print("El vector reducido es ",Vector)

    elif opcion==8:
        Copia=(tamanio-1)*['']
        print("Llenar el vector con elementos aleatorios)")
        for i in range(tamanio):
            Vector[i]= int(math.trunc(random.random()*100))
        print ("El vector ingresado es ",Vector)
        valor=int(input("¿Qué valor del vector desea elimninar?: "))
        if valor in Vector:
            reg=Vector.index(valor)
        i=0
        while i<reg:
            for i in range(tamanio-1):
                Copia[i]=Vector[i]
                i+1
        for i in range(reg,tamanio-1):
            Copia[i]=Vector[i+1]
        Vector=Copia
        print("El vector reducido es ",Vector)
    