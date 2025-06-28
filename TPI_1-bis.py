print("----------------------------------------")
print("CALCULADORA DE GASTOS MENSUALES")
print("----------------------------------------")

presu=int(input("El presupuesto disponible es de $ "))
gasto=0
def funcion(gasto,presu):
    gasto=int(input("Ingresar nuevo gasto: "))
    if gasto==0:
        print("-----------------------------------------")
        print(f"Aún le restan $ {presu} para gastar - Gracias por usar nuestro sistema")
        print("-----------------------------------------")
        exit()
    elif gasto>presu:
        print("-----------------------------------------")
        print(f"El gasto realizado excede su presupuesto. Su saldo es $ {presu}")
        print("-----------------------------------------")
    else:        
        presu=presu-gasto
    return presu
while gasto<presu:
    resul=funcion(gasto,presu)
    print("-----------------------------------------")
    print("El presupuesto disponible es de $ ",resul)
    print("-----------------------------------------")
    presu=resul
