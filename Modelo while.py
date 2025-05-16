print("-------------------------------------------------------------")
print("ESTE ES EL MODELO DE CÓMO SE USA 'while' EN PYTHON")
print("-------------------------------------------------------------")

# Primero creamos una variable en la que guardamos un valor

variable = int(input("Ingresar un número (del 1 al 12): "))

# Ahora establecemos una condición. Mientras se cumple, el ciclo continuará.
# Cuando deje de cumplirse, el ciclo cesa

while variable<=12:
    print("-------------------------------------------------------------")
    print("               El valor de la variable es ",variable)
    
    variable=variable+1

print("-------------------------------------------------------------")



