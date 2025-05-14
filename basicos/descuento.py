print("--------------------------------------------------------------")
print("CÁLCULO DEL PRECIO DE UN ELECTRODOMÉSTICO)")
print("--------------------------------------------------------------")

precio_lista=int(input("Ingresar el precio de lista del electrodoméstico: "))
IVA=1.21
marca=str(input("Ingresar la marca del electrodoméstico: "))

if marca=="NOSY" or marca=="Nosy" or marca=="nosy" and precio_lista>=2000:
    precio_final=precio_lista*.85*IVA
    print("-------------------------------------------------------------------------")
    print ("El precio del electrodoméstico es de $ : ",(precio_final))
    print("-------------------------------------------------------------------------")
elif marca=="NOSY" or marca=="Nosy" or marca=="nosy" and precio_lista<2000:
    precio_final=precio_lista*.95*IVA
    print("-------------------------------------------------------------------------")
    print ("El precio del electrodoméstico es de $ : ",precio_final)
    print("-------------------------------------------------------------------------")

elif marca!="NOSY" or marca!="Nosy" or marca!="nosy" and precio_lista>2000:
    precio_final=precio_lista*.9*IVA
    print("-------------------------------------------------------------------------")
    print ("El precio del electrodoméstico es de $ : ",precio_final)
    print("-------------------------------------------------------------------------")
elif marca!="NOSY" or marca!="Nosy" or marca!="nosy" and precio_lista<2000:
    precio_final=precio_lista*1*IVA
    print("-------------------------------------------------------------------------")
    print ("El precio del electrodoméstico es de $ : ",precio_final)
    print("-------------------------------------------------------------------------")

