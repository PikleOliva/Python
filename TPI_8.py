import math
print("----------------------------------------")
print("REGISTRO DE EJERCICIOS SEMANALES   ")
print("----------------------------------------")
limite=int(input("Cuál es el mínimo de ejercitación deseado?: "))
actividad=0
total=0

j=1
for i in range(7):
    actividad=int(input(f"¿Cuántos minutos se ejercitó el día {j}? "))
    total=total+actividad
    j=j+1
media=round(total/7, 2)
print("------------------------------------------------")
print("Usted se entrenó un promedio de ",media," minutos por díaºC")
print("El tiempo sugerido de entrenamiento es de ",limite," minutos diarios")
if media<limite:
    print("Le aconsejamos entrenar un poco más")
print("------------------------------------------------")
