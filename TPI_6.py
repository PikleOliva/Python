print("----------------------------------------")
print("ESTADÍSTICA DE DONACIONES")
print("----------------------------------------")
donaciones=1
total=0
donantes=0
max=0
i=1
while donaciones!=0:
    donaciones=int(input(f"Ingresar la donación del donante Nº {i}: "))
    total=total+donaciones
    donantes=donantes+1
    i=i+1
    if donaciones>max:
        max=donaciones
    if donaciones==0:
        donantes=donantes-1
    
print("------------------------------------------------")
print("El total de donaciones alcanzado fue de ",total)
print("El promedio de donaciones alcanzado fue de ",total/donantes)
print("La donaciónmayor fue de ",max)
print("El total de donantes que aportaron fue de ",donantes)
print("------------------------------------------------")
