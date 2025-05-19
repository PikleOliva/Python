import random
from math import *

print("-------------------------------------------------------------")
print("MOSTRAR EL SUELDO MAYOR Y SU NÚMERO DE LEGAJO")
print("-------------------------------------------------------------")

cant=int(input("¿Cuántos empleados hay que verificar?: "))
mayor=0

for i in range(cant):
    sal=int(input("ingresar el sueldo del empleado: "))
    
    if sal>mayor:
        
        mayor=sal
        m=i+1
    
    
print("-------------------------------------------------------------")
print("El salario mayor es de $ ",mayor," y le corresponde al empleado legajo ",m)
print("-------------------------------------------------------------")

