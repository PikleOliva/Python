print("-------------------------------------------------------")
print("Complemento3: CRIBA DE ERATÓSTENES.")
print("-------------------------------------------------------")
#inicializar
#LLenar B con True, suponiendo que todos son primos
B = 1000*[True]
N = []
#Llenar N con elementos de 1 a 100
for i in range(1, 1000+1): 
    N.append(i) 
#Proceso 
# #como 1 no es primo, y se encuentra la posicion 0 
B[0] = False 
for i in range(1, 999): 
    for j in range(i+1, 1000): 
        if N[j] % N[i] == 0: 
            B[j] = False 
for i in range(1000): 
    #Si el valor de B[i] = 1 
    if B[i]: print(N[i])