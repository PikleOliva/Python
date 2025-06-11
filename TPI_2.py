print("----------------------------------------")
print("CALCULADORA DE CARGAS DE COMBUSTIBLE")
print("----------------------------------------")

carga=1
consumo=0
litros=0
while carga!=0:

    carga=int(input("Ingresar cuantos litros cargó (0 para salir): "))
    litros=litros+carga
    if carga<5 and carga!=0:
        print("----------------------------------------")
        print("¡¡¡OJO AL PIOJO!!! Se ha cargado por debajo del mínimo")
        print("----------------------------------------")
    
print("----------------------------------------")   
print("Los carga mensual de combustible ha sido de ",litros)
print("----------------------------------------")   