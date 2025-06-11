print("----------------------------------------")
print("REGISTRO DE TEMPERATURAS SEMANALES   ")
print("----------------------------------------")
tempe=0
total=0
contador=0
j=1
for i in range(7):
    tempe=float(input(f"Ingresar la temperatura del día {j}: "))
    total=total+tempe
    j+1
    if tempe>30:
        contador=contador+1


print("------------------------------------------------")
print("La media de las temperaturas semanales fue de ",total/7," grados")
print(contador," días se registraron temperaturas superiores  los 30º")
