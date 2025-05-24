#Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento4: CALCULA EL DÍA SIGUIENTE.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese la fecha: ")
d = int( input("Día: "))
m = int( input("Mes: "))
a = int( input("Año: "))
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")

if m==2:
    if a%4==0 or a%400==0 and a%100!=0:
        if d > 0 and d < 29 :
            print("Mañana es:",d+1,"/",2,"/",a)
        else:
            print("Mañana es: ",1,"/",3,"/",a)
                
    else:
            if d > 0 and d < 28 :
                print("Mañana es:",d+1,"/",2,"/",a)
            else:
                print("Mañana es:", 1, 3, a)
            
else:    
    if d==31 and m==12:
        print("Mañana es:",1,"/",1,"/",a+1)
    
    if m==4 or m==6 or m==9 or m==11:   
        if d > 0 and d < 30 :
            print("Mañana es:",d+1,"/",m,"/",a)
        else:
            print("Mañana es: ",1,"/",m+1,"/",a)
            
    else:   
        if d > 0 and d < 31 :
            print("Mañana es:",d+1,"/",m,"/",a)
        else:
            print("Mañana es: ",1,"/",m+1,"/",a)
        
                
