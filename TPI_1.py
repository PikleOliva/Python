print("----------------------------------------")
print("CALCULADORA DE GASTOS MENSUALES")
print("----------------------------------------")

presu=100000
gasto=1
consumo=0
print("El presupuesto disponible es de $ ",presu)
while gasto!=0 and consumo<presu:

    gasto=int(input("Ingresar el nuevo gasto: "))
    anterior=consumo
    consumo=consumo+gasto
    if consumo>presu:
        print("----------------------------------------")
        print("Los gastos han excedido el presupuesto disponible")
        # print("Los gastos mensuales han sido de $ ",anterior)
        print("----------------------------------------")
        consumo=anterior
        gasto=0
    
print("----------------------------------------")   
print("Los gastos mensuales han sido de $ ",consumo)
print("----------------------------------------")   