print("-------------------------------------------------------------")
print("CALCULO DEL DÍA SIGUIENTE")
print("-------------------------------------------------------------")

dia=int(input("ingresar el día (1-30): "))
mes=int(input("ingresar el mes (1-12): "))
año=int(input("ingresar el año: "))

if dia>0 and dia<30:
    dia=dia+1
elif mes>0 and mes<12:
    dia=1
    mes=mes+1
else:
    dia=1
    mes=1
    año=año+1

print("-------------------------------------------------------------")
print("Mañana será ",dia,"/",mes,"/",año)
print("-------------------------------------------------------------")
