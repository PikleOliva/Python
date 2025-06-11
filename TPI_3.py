print("----------------------------------------")
print("HABITOS SALUDABLES")
print("----------------------------------------")
total=0
for i in range(7):
    vasos=int (input(f"Cuántos vasos tomó el día {i+1}: "))
    total=total+vasos
    promedio=total/7


print("----------------------------------------")
print("Usted ha consumido ",promedio," vasos de agua por día")
if promedio<8:
    print("Debería consumir como mínimo 8 vasos diarios")
print("----------------------------------------")   