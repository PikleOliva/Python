print("-------------------------------------------------------------")
print("ESCRIBIR LOS ´DÍGITOS QUE INTEGRAN UN NÚMERO ")
print("-------------------------------------------------------------")

status_code = 600

match status_code:
    case 200 as code:
        print(f"Código de estado: {code} (Ok)")
    case 400:
        print("Error del cliente")
    case 500:
        print("Error del servidor")
    case _:
        print("Código de estado desconocido")