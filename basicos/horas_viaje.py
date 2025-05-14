print("--------------------------------------------------------------")
print("CÁLCULO DEL TIEMPO QUE INSUMEN DOS VIAJES (En horas y minutos)")
print("--------------------------------------------------------------")

hora_1=int(input("Ingresar la cantidad de horas del primer viaje: "))
min_1=int(input("Ingresar la cantidad de minutos del primer viaje: "))
hora_2=int(input("Ingresar la cantidad de horas del segundo viaje: "))
min_2=int(input("Ingresar la cantidad de minutos del segundo viaje: "))

horas_total=hora_1+hora_2
min_total=min_1+min_2
if min_total>60:
    min_total=min_total-60
    horas_total=horas_total+1

print("-------------------------------------------------------------------------")
print ("El tiempo insumido en los dos viajes fue de ",horas_total," horas y ",min_total," minutos")
print("-------------------------------------------------------------------------")

horas_extra=min_total//60
min_total_1=min_total % 60

horas_total_1=horas_total+horas_extra

print("-------------------------------------------------------------------------")
print ("El tiempo insumido en los dos viajes fue de ",horas_total_1," horas y ",min_total_1," minutos")
print("-------------------------------------------------------------------------")
