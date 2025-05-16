print("-------------------------------------------------------------")
print("ESTE ES EL MODELO DE CÓMO SE USA 'if' EN PYTHON")
print("-------------------------------------------------------------")

# Primero creamos una variable en la que guardamos un valor

variable = int(input("Ingresar un número (del 1 al 12): "))

# Ahora empezamos con los 'if' para seleccionar la opcion elegida

mes = " una opción incorrecta"

if variable == 1:
    mes = "enero"
elif variable == 2:
    mes = "febrero"
elif variable == 3:
    mes = "marzo"
elif variable == 4:
    mes = "abril"
elif variable == 5:
    mes = "mayo"
elif variable == 6:
    mes = "junio"
elif variable == 7:
    mes = "julio"
elif variable == 8:
    mes = "agosto"
elif variable == 9:
    mes = "SEPTIEMBRE!!!!"
elif variable == 10:
    mes = "octubre"
elif variable == 11:
    mes = "noviembre"
elif variable == 12:
    mes = "diciembre"

# Y ahora imprimo resultados

print("-------------------------------------------------------------")
print("               El mes elegido es ",mes)
print("-------------------------------------------------------------")


