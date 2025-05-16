print("-------------------------------------------------------------")
print("MODELO DE USO DE 'match' Y 'case'")
print("-------------------------------------------------------------")

# Coincidencia simple

"""x = int(input("Seleccionar una opción (1, 2, o 10): "))

match x:
    case 1: print("x es 1")
    case 2: print("x es 2")
    case 10: print("x es 10")
    case _:  print("x no coincide con ninguno de los casos anteriores")"""

# Usando as 

opcion = int(input("Seleccionar una opción (200, 400, 500) "))
match opcion:
    case 200 as code:
        print(f"Código de estado: {code} (Ok)")
    case 400:
        print("Error del cliente")
    case 500:
        print("Error del servidor")
    case _:
        print("Código de estado desconocido")

# Coincidencia con múltiples valores (usando |)

"""dia = str(input("Elegir el día (lun-mar-mie-jue-vie-sab-dom)"))

match dia:
    case "Lun" | "Mar" | "Mie" | "Jueves" | "Viernes":    print("Es un día de la semana")
    case "Sab" | "Dom":    print("Es un fin de semana")  
    case _:      print("Día inválido")
"""
