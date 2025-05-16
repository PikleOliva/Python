print("-------------------------------------------------------------")
print("ESTE ES EL MODELO DE CÓMO SE HACE UNA FUNCIÓN EN PYTHON")
print("-------------------------------------------------------------")

# Primero hacemos la función con las opciones disponibles

selector = { 
    1: "Enero", 
    2: "Febrero", 
    3: "Marzo", 
    4: "Abril", 
    5: "Mayo", 
    6: "Junio", 
    7: "Julio", 
    8: "Agosto", 
    9: "Septiembre", 
    10: "Octubre", 
    11: "Noviembre", 
    12: "Diciembre" 
} 

# Creamos una variable en la que guardaremos la opción seleccionada

variable = int( input("Ingresar el número de mes: "))

# Y ahora creamos otra, a la que la variable creada anteriormente 
# le pasará el valor correspondiente a la opción seleccionada. 
# Tiene como alternativa un texto para el caso de que la selección no esté entre las disponibles


mes = selector.get(variable, "Mes inválido")

# Finalmente imprimimos la selección

print("-------------------------------------------------------------")
print("                          ",mes)
print("-------------------------------------------------------------")