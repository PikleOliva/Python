import math
print("----------------------------------------")
print("REGISTRO DE TEMPERATURAS SEMANALES   ")
print("----------------------------------------")
limite=int(input("Cuál es el límite de temperatura deseado?: "))
tempe=0
total=0
contador=0
j=1
for i in range(7):
    tempe=math.trunc(float(input(f"Ingresar la temperatura del día {j}: ")))
    total=total+tempe
    j=j+1
    if tempe>limite:
        contador=contador+1

media=round(total/7, 2)
if contador==0:
    print("------------------------------------------------")
    print("La media de las temperaturas semanales fue de ",media,"ºC")
    print("No hubo días con temperaturas por encima de ",limite,"ºC")
    print("------------------------------------------------")
else:
    print("------------------------------------------------")
    print("La media de las temperaturas semanales fue de ",media,"ºC")
    print("En ",contador," días se registraron temperaturas superiores los ",limite,"ºC")
    print("------------------------------------------------")