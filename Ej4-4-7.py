print("-------------------------------------------------------------")
print("CALCULO DE LAS RAÍCES")
print("-------------------------------------------------------------")

coefA=int(input("Ingresar el primer coeficiente (a): "))
coefB=int(input("Ingresar el segundo coeficiente (b): "))
coefC=int(input("Ingresar el tercer coeficiente (c): "))

if coefB**2-4*coefA*coefC<0:
    
    print("-------------------------------------------------------------")
    print("La ecuación no tiene raíces reales")
    print("-------------------------------------------------------------")
elif coefB**2-4*coefA*coefC==0:
    raiz=float((-coefB+(coefB**2-4*coefA*coefC)**0.5)/(2*coefA))
    print("-------------------------------------------------------------")
    print("La ecuación tiene una única raíz real en x = ",raiz)
    print("-------------------------------------------------------------")
else:
    raiz1=float((-coefB+(coefB**2-4*coefA*coefC)**0.5)/(2*coefA))
    raiz2=float((-coefB-(coefB**2-4*coefA*coefC)**0.5)/(2*coefA))
    print("-------------------------------------------------------------")
    print("La ecuación tiene dos raíces reales en x1 = ",raiz1," y en x2 = ",raiz2)
    print("-------------------------------------------------------------")