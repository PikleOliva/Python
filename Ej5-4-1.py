print("-------------------------------------------------------------")
print("CALCULAR EL CAPITAL (C) LUEGO DE COLOCARLO A UN DETERMINADO INTERÉS SIMPLE (I) POR (t) TIEMPO")
print("-------------------------------------------------------------")

# Ingresamos los datos, c, i t

c=-1
i=0
t=0
#j=int
while c<0 and i>=0 and i<=100 and t>=0:
    c=int(input("¿Cuánto vas a invertir?: "))
    i=int(input("¿Cuál es la tasa de interés?: "))
    t=int(input("¿Por cuanto tiempo (años) vas a colocar?: "))
    ci=c
for j in range(t):
    c=c*(1+i/100)

print("-------------------------------------------------------------")
print("El capital inicial era ",ci)
print("El tiempo de colocación fue de ",t," años")
print("´La tasa de interés fue del ",i," o/o anual")
print("-------------------------------------------------------------")
print("Tu capital ahora es de ",c," $")
print("-------------------------------------------------------------")
