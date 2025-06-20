import math
print("----------------------------------------")
print("CONSUMOS DE COMBUSTIBLE")
print("----------------------------------------")
resto=0
carga=0
consumo=0
opcion=int(input("Selecciones una opción (1=Carga, 2=Consumo, 0-Salir) "))


while opcion !=0:

    if opcion==1:
        carga=int(input("Ingresar los litros cargados: "))
        resto=resto+carga
        if resto<3.5:
            print("----------------------------------------")
            print("ATENCIÓN, la autonomía es menor a 50 km")
            print("----------------------------------------")
        elif resto>=3.5:
            print("----------------------------------------")
            print("La autonomía restante es de ",round((resto*100/7), 2)," kilómetros")
            print("----------------------------------------")
        opcion=int(input("Selecciones una opción (1=Carga, 2=Consumo, 0-Salir) "))
    elif opcion==2:
        consumo=int(input("Ingresar los litros consumidos: "))
        
        if resto<consumo:
            print("----------------------------------------")
            print("Imposible haber consumido más de lo que había en el tanque")
            print("Verifique su consumo")
            print("----------------------------------------")
            opcion=int(input("Selecciones una opción (1=Carga, 2=Consumo, 0-Salir) "))
        else:
            resto=resto-consumo
        
        if resto<3.5:
            print("----------------------------------------")
            print("ATENCIÓN, la autonomía es menor a 50 km")
            print("La autonomía restante es de ",round((resto*100/7),2)," kilómetros")
            print("----------------------------------------")
        elif resto>=3.5:
            print("----------------------------------------")
            print("La autonomía restante es de ",round((resto*100/7),2)," kilómetros")
            print("----------------------------------------")
        opcion=int(input("Selecciones una opción (1=Carga, 2=Consumo) "))
    