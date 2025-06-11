import math
print("----------------------------------------")
print("CONSUMOS DE COMBUSTIBLE")
print("----------------------------------------")
resto=0
carga=0
consumo=0
opcion=input("Selecciones una opción (1=Carga, 2=Consumo) ")

while opcion !=0:

    if opcion==1:
        carga=int(input("Ingresar los litros cargados: "))
        resto=resto+carga
        if resto<3.5:
            print("ATENCIÓN, la autonomía es menor a 50 km")
        elif resto>=3.5:
            print("La autonomía restante es de ",resto*100/7," kilómetros")

    elif opcion==2:
        consumo=int(input("Ingresar los litros consumidos: "))
        resto=resto-consumo
        if resto<3.5:
            print("ATENCIÓN, la autonomía es menor a 50 km")
        elif resto>=3.5:
            print("La autonomía restante es de ",resto*100/7," kilómetros")

    #else:
     #   print("La ppción no está habilitada")

    if resto<3.5:
        print("ATENCIÓN, la autonomía es menor a 50 km")
    elif resto>=3.5:
        print("La autonomía restante es de ",resto*100/7," kilómetros")
