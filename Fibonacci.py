print("-------------------------------------------------------")
print("              TÉRMINOS DE LA SUCESIÓN DE FIBONACCI")
print("-------------------------------------------------------")

ter_1=1
ter_2=0
ter=0
largo = int(input("Cuántos términos de la sucesión desea mostrar?:"))
print("")
print("0, 1",end=", ")
for i in range(largo-3):
    ter=ter_1+ter_2
    ter_2=ter_1
    ter_1=ter
    print(ter,end=", ")
print(ter_1+ter_2)






print("-------------------------------------------------------")

print("-------------------------------------------------------")
