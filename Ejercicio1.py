# -*- coding: utf-8 -*-
#Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Ejercicio1: CALCULAR DISTANCIA.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese la velocidad y el tiempo de la unidad móvil")
#convirtiendo entrada a Entero
velocidad = float( input("Velocidad (en km/h): ") )
tiempo = int( input("Tiempo( expresado en horas): ") )
#Proceso
distancia = velocidad * tiempo
#Salida
print("La distancia recorrida es de: ", distancia)