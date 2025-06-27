print("----------------------------------------")
print("CALCULADORA DE GASTOS MENSUALES")
print("----------------------------------------")

presu=int(input("El presupuesto disponible es de $ "))
consumo=0

def funcion():
    consumo=int(input("Ingresar nuievo gasto: "))
    return consumo

while consumo<presu:
    print(consumo)
    anterior=consumo
    funcion()
    print(consumo)

#     gasto=int(input("Ingresar el nuevo gasto: "))
#     anterior=consumo
#     consumo=consumo+gasto
#     if consumo>presu:
#         print("----------------------------------------")
#         print("Los gastos han excedido el presupuesto disponible")
#         # print("Los gastos mensuales han sido de $ ",anterior)
#         print("----------------------------------------")
#         consumo=anterior
#         gasto=0
    
# print("----------------------------------------")   
# print("Los gastos mensuales han sido de $ ",consumo)
# print("----------------------------------------")   