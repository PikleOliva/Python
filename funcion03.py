import math

def rayas(n):
    for i in range(n):
        print("-",end=" ")
    print("")
def supTriangulo(base, altura):
    area=base*altura/2
    return area
def circulo(radio):
    area=math.pi*radio**2
    return area

rayas(40)
print("Calcular el el volumen de un prisma de base triangular")
rayas(40)

base=int(input("Ingresar el valor de la base de la base: "))
alt=int(input("Ingresar el valor de la altura de la base: "))
altura=int(input("Ingresar la altura del prisma: "))
volumen=supTriangulo(base,alt)*altura
print("El volunmen del prisma es :",volumen)

rayas(40)
print("Volumen de un cilindro, un cono y un esfera de radio r")
rayas(40)
radio=int(input("Ingresar el valor del radio de la base: "))
alt=int(input("Ingresar el valor de la altura del cilindro y el cono: "))
volCil=round((circulo(radio)*alt),2)
volCon=round((1/3)*circulo(radio)*alt,2)
volEsf=round((4/3)*radio*circulo(radio),2)
print("El volumen del cilindro es ",volCil)
print("El volumen del cono es ",volCon)
print("El volumen de la esfera es ",volEsf)

