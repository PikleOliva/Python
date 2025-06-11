print("----------------------------------------------")
print("      PROGRAMA VACACIONES DEL PERSONAL")
print("----------------------------------------------")

nombre=input("Ingresar el nombre del trabajador: ")
depto=int(input("Indicar a qué departamento pertenece "
"(1- Atención al cliente; 2- Logística: 3- Gerencia): "))
antig=int(input("Ingresar la antigüedad del trabajadore en la empresa: "))

match depto:
    case 1:
        if antig>0 and antig<1:
            print("El trabajador no tiene antigüedad" \
            " suficiente para gozar de vacaciones")
        elif antig==1:
            print("----------------------------------------------")
            print("Al trabajador ",nombre," le corresponden " \
            "6(seis) días de vacaciones")
            print("----------------------------------------------")
            
        elif antig>=2 and antig<=6:
            print("----------------------------------------------")
            print("Al trabajador ",nombre," le corresponden " \
            "14(catorce) días de vacaciones")
            print("----------------------------------------------")
        elif antig>=7:
            print("----------------------------------------------")
            print("Al trabajador ",nombre," le corresponden " \
            "20(veinte) días de vacaciones")
            print("----------------------------------------------")
    case 2:
       
       
                if antig>0 and antig<1:
                    print("El trabajador no tiene antigüedad" \
                    " suficiente para gozar de vacaciones")
                elif antig==1:
                    print("----------------------------------------------")
                    print("Al trabajador ",nombre," le corresponden " \
                    "7(siete) días de vacaciones")
                    print("----------------------------------------------")
                elif antig>=2 and antig<=6:
                    print("----------------------------------------------")
                    print("Al trabajador ",nombre," le corresponden " \
                    "15(quince) días de vacaciones")
                    print("----------------------------------------------")
                elif antig>=7:
                    print("----------------------------------------------")
                    print("Al trabajador ",nombre," le corresponden " \
                    "22(veintidós) días de vacaciones")
                    print("----------------------------------------------")
    case 3:
       
       
                if antig>0 and antig<1:
                    print("El trabajador no tiene antigüedad" \
                    " suficiente para gozar de vacaciones")
                elif antig==1:
                    print("----------------------------------------------")
                    print("Al trabajador ",nombre," le corresponden " \
                    "10(diez) días de vacaciones")
                    print("----------------------------------------------")
                elif antig>=2 and antig<=6:
                    print("----------------------------------------------")
                    print("Al trabajador ",nombre," le corresponden " \
                    "20(veinte) días de vacaciones")
                    print("----------------------------------------------")
                elif antig>=7:
                    print("----------------------------------------------")
                    print("Al trabajador ",nombre," le corresponden " \
                    "30(treinta) días de vacaciones")
                    print("----------------------------------------------")
    case _:
        print("El código ingresado es inexistente")
