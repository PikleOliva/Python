print ("----------------------------------------------------------------")
print ("ESTE ES UN INVENTO QUE NO CREO QUE FUNCIONE")
print ("----------------------------------------------------------------")

opcion = int(input("Ingresar la opción de comida elegida: "))

Funcion = {
    1:'matambre',
    2:'ensalada rusa',
    3:'roast beef',
    4:'flan con dulce de leche'
}
print ("----------------------------------------------------------------")
print (Funcion.get(opcion, "opcion incorrecta"))
print ("----------------------------------------------------------------")

selec = int(input("Ingresar opcion de estado de ánimo elegido: "))
Seleccion = {
    1:"vamos bien",
    2:"vamos regular",
    3:"vamos como la mierda"
}
print ("----------------------------------------------------------------")
print (Seleccion.get(selec, "opcion incorrecta"))
print ("----------------------------------------------------------------")

print ("----------------------------------------------------------------")
print ("¿En qué mes estamos?, ¡AH!")
print ("----------------------------------------------------------------")

mes = {
    1:'Estamos en enero',
    2:'Estamos en febrero',
    3:'Estamos en marzo',
    4:'Estamos en abril',
    5:'Estamos en mayo',
    6:'Estamos en junio',
    7:'Estamos en julio',
    8:'Estamos en agosto',
    9:'Estamos en septiembre (el mejor mes del año porque nació el Piklito)',
    10:'Estamos en octubre',
    11:'Estamos en noviembre',
    12:'Estamos en diciembre',
    
}
meee = int(input("Ingresar el número de mes elegido: "))
print ("----------------------------------------------------------------")
print (mes.get(meee, "opcion incorrecta"))
print ("----------------------------------------------------------------")
