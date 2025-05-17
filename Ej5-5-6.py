from math import * 
print("-------------------------------------------------------------")
print("INVERTIR LOS DIGITOS DE UN NÚMERO")
print("-------------------------------------------------------------")

n=int(input("Ingresar un número: "))
noriginal=n
nfinal=0
naux=0

while n>10:
    naux=(n%10)
    #print(naux)
    nfinal=(nfinal+naux)*10
    #print(nfinal)
    n=int(n/10)
    #print(n)

nfinal=nfinal+n
#print(nfinal)

print("-------------------------------------------------------------")
print("El número ",noriginal," con los dígitos invertidos es ",nfinal)
print("-------------------------------------------------------------")
