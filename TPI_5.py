print("----------------------------------------")
print("CONTROL DE STOCK DE UN PRODUCTO")
print("----------------------------------------")
stock=int(input("Ingresar el stock inicial de producto: "))
total=stock
while stock>0:
    venta=int(input("Ingresar la cantidad de producto vendida: "))
    if venta==0:
        print("------------------------------------------------")
        print("Gracias por usar este programa. El stock actualizado es de ",stock," productos")
        print("------------------------------------------------")
    elif venta>stock:
        print("------------------------------------------------")
        print("No hay stock disponible para esta venta. El stock actualizado es de ",stock," productos")
        print("------------------------------------------------")
    else:
        stock=stock-venta
        if stock<total*0.1:
            print("------------------------------------------------")
            print("¡¡¡OJO AL PIOJO!!! El stock está por debajo del 10'%' del inicial")
            print("------------------------------------------------")
    print("El stock remanente es de ",stock)