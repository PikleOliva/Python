print("----------------------------------------")
print("REGISTRO DE NOTAS DE LOS ALUMNOS")
print("----------------------------------------")
for i in range (10):
    nota=int (input(f"Nota obtenida por el alumno {i+1}: "))
    while nota<0 or nota>10:
        print ("La nota debe estar entre 0 y 10")
        nota=int (input(f"Nota obtenida por el alumno {i+1}: "))
    if nota < 6:
        print("El alumno resultó DES-A-PRO-BA-DO")
        print()
    else:
        print("El alumno resultó A-PRO-BA-DO")
        print()